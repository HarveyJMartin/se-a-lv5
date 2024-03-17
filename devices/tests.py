from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import devices
from .forms import DeviceForm
# Create your tests here.

class DevicesViewsTestCase(TestCase):
    def setUp(self):
        # Create user accounts for testing 
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.admin_user = User.objects.create_user(username='admin', password='12345', is_staff=True)
        self.client = Client()

        # Create devices for testing
        self.device1 = devices.objects.create(device_brand='Test Brand 1', device_model='Test Model 1', os_version='1')
        self.device2 = devices.objects.create(device_brand='Test Brand 2', device_model='Test Model 2', os_version='2')

    def test_device_list(self):
        # Log in as a non staff user
        self.client.login(username='testuser', password='12345')
        
        response = self.client.get(reverse('devices:all_devices'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.device1, response.context['devices'])
        self.assertIn(self.device2, response.context['devices'])

# Test to make sure admins can access the create device page with a get request 
    def test_get_create_device_as_admin(self):
        # Log in as an admin
        self.client.login(username='admin', password='12345')
        response = self.client.get(reverse('devices:create_device'))
        # Checking server response
        self.assertEqual(response.status_code, 200)
        # Checking correct template is used to render the page
        self.assertTemplateUsed(response, 'create_device.html')
        # Checking the form is an instance of DeviceForm. Validates it has been correctly passed to the template 
        self.assertIsInstance(response.context['form'], DeviceForm)

# Test create device with invalid input, to make sure a device is not created
    def test_create_device_with_invalid_input(self):
        # Log in as an admin
        self.client.login(username='admin', password='12345')
        device_count_before = devices.objects.count()
        # The form is being submitted with empty fields
        response = self.client.post(reverse('devices:create_device'), {
            'device_brand': '',
            'device_model': '',
            'os_version': '1'
        })
        # Checking device count remains the same (meaning no devices were created)
        self.assertEqual(devices.objects.count(), device_count_before)
        # Confirm form was re-rendered with errors successfully
        self.assertEqual(response.status_code, 200)
        # Checking the form contains the errors 
        self.assertTrue(response.context['form'].errors)

# Testing that a non admin can not create a device
    def test_create_device_access_as_non_admin(self):
        # Log in as a normal user
        self.client.login(username='user', password='12345')
        response = self.client.get(reverse('devices:create_device'))
        # Checking a non ok status is returned
        self.assertNotEqual(response.status_code, 200)  # Should return redirect or forbidden status

