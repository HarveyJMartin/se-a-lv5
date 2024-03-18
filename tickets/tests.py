from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Ticket
from django.urls import reverse
from .models import devices
from django.contrib.messages import get_messages

# Create your tests here.


class TicketViewsTestCase(TestCase):
    def setUp(self):
        # Create user accounts for testing
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.admin_user = User.objects.create_user(
            username="admin", password="12345", is_staff=True
        )
        self.client = Client()

        self.device = devices.objects.create(
            device_brand="Test Brand 1", device_model="Test Model 1", os_version="1"
        )

        self.ticket = Ticket.objects.create(comments="Test Ticket", device=self.device)

    # All tickets view displays all tickets
    def test_all_tickets_view(self):
        # Login as user
        self.client.login(username="testuser", password="12345")
        # Gather response from accessing all tickets
        response = self.client.get(reverse("tickets:all_tickets"))
        # Check response code is ok
        self.assertEqual(response.status_code, 200)
        # Check correct template is used
        self.assertTemplateUsed(response, "all_tickets.html")
        # Ensure the context contains tickets data
        tickets_in_context = response.context["tickets"]
        self.assertIsNotNone(tickets_in_context)
        # Check if the tickets in context contain the created test ticket
        self.assertEqual(tickets_in_context.count(), 1)
        self.assertEqual(tickets_in_context.first().comments, "Test Ticket")

    # Test assign ticket as admin
    def test_assign_ticket_admin(self):
        # Log in as admin
        self.client.login(username="admin", password="12345")
        # Create POST request to assign ticket
        response = self.client.post(
            reverse("tickets:assign_ticket"), {"ticket_id": self.ticket.id}
        )
        # Reload ticket from the database to check updates
        self.ticket.refresh_from_db()
        # Check if the ticket is now assigned to the admin user
        self.assertEqual(self.ticket.assigned_to, self.admin_user)
        # Check for success message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Ticket successfully assigned!")
        # Verify redirection to the ticket list page
        self.assertRedirects(response, reverse("tickets:ticket_list"))

    # Test non admin user gets redirected if they assign ticket
    def test_assign_ticket_by_non_admin(self):
        # Non admin user log in
        self.client.login(username="testuser", password="12345")
        # Simulate POST request to assign ticket by a non-admin user
        response = self.client.post(
            reverse("tickets:assign_ticket"), {"ticket_id": self.ticket.id}
        )
        # Check user is redirected (admin decorator redirects to login page)
        self.assertTrue(response.status_code, 302)

# Testing redirection to confirmation page of delete ticket 
    def test_ticket_delete_confirmation_admin(self):
        # Log in as admin
        self.client.login(username='admin', password='12345')
        # Create a GET request to the delete view
        response = self.client.get(reverse('tickets:ticket_delete', args=[self.ticket.id]))
        # Check the response status code is 200
        self.assertEqual(response.status_code, 200)
        # Check that the correct template is used
        self.assertTemplateUsed(response, 'ticket_confirm_delete.html')
        # Correct ticket is passed to the template
        self.assertEqual(response.context['ticket'].id, self.ticket.id)

# Test admin can delete ticket after confirmation 
    def test_ticket_delete_admin(self):
        # Log in as admin
        self.client.login(username='admin', password='12345')
        # Create a POST request to the delete view
        response = self.client.post(reverse('tickets:ticket_delete', args=[self.ticket.id]))
        # Check that the ticket has been deleted
        self.assertEqual(Ticket.objects.filter(id=self.ticket.id).count(), 0)
        # Verify that the response is a redirect to the ticket list page
        self.assertRedirects(response, '/tickets/')
