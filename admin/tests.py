from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import AdminRequest
from django.contrib.messages import get_messages


class AdminViewsTestCase(TestCase):
    def setUp(self):
        # Create a regular user
        self.user = User.objects.create_user(username="testuser", password="12345")
        # Create an admin user
        self.admin_user = User.objects.create_user(
            username="admin", password="12345", is_staff=True
        )
        # Create an admin request
        self.admin_request = AdminRequest.objects.create(
            user=self.user, status="pending"
        )
        # Initialize the test client
        self.client = Client()

    # Testing admin can approve an admin access request
    def test_approve_request(self):
        # Log in as admin
        self.client.login(username="admin", password="12345")
        # Create the URL for approving the request
        url = reverse("admin:approve_request", args=[self.admin_request.id])
        # Perform the approve action and follow the redirect
        response = self.client.get(url, follow=True)
        # Fetch the updated admin request
        self.admin_request.refresh_from_db()
        # Check if the request status is now 'approved'
        self.assertEqual(self.admin_request.status, "approved")
        # Check if the user is now an admin
        self.user.refresh_from_db()
        self.assertTrue(self.user.is_staff)
        # Check that the success message was added
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Request approved!")
        # Check if the user is redirected to the manage page
        self.assertRedirects(
            response,
            reverse("admin:manage_admin_requests"),
            status_code=302,
            target_status_code=200,
        )

    # Test admin can reject admin access request
    def test_reject_request(self):
        # Log in as admin
        self.client.login(username="admin", password="12345")
        # Create the URL for rejecting the request
        url = reverse("admin:reject_request", args=[self.admin_request.id])
        # Perform the reject action and follow the redirect
        response = self.client.get(url, follow=True)
        # Fetch the updated admin request
        self.admin_request.refresh_from_db()
        # Check if the request status is now 'rejected'
        self.assertEqual(self.admin_request.status, "rejected")
        # Check that the success message was added
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Request rejected!")
        # Check if the user is redirected to the manage page
        self.assertRedirects(
            response,
            reverse("admin:manage_admin_requests"),
            status_code=302,
            target_status_code=200,
        )

    # Test non admin can not approve admin access request
    def test_non_admin_cannot_approve_request(self):
        # Log in as the regular user
        self.client.login(username="testuser", password="12345")
        # Attempt to approve the admin request
        approve_url = reverse("admin:approve_request", args=[self.admin_request.id])
        response = self.client.get(approve_url)
        # Check that the user is not allowed to approve the request
        # You might want to check for a specific response like a 403 Forbidden
        self.assertNotEqual(response.status_code, 200)
        self.assertEqual(response.status_code, 302)

    # Test non admin can not reject admin access request
    def test_non_admin_cannot_reject_request(self):
        # Log in as the regular user
        self.client.login(username="testuser", password="12345")
        # Attempt to reject the admin request
        reject_url = reverse("admin:reject_request", args=[self.admin_request.id])
        response = self.client.get(reject_url)
        # Check that the user is not allowed to reject the request
        self.assertNotEqual(response.status_code, 200)
        self.assertEqual(response.status_code, 302)
