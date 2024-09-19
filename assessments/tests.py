from django.test import TestCase
from django.urls import reverse
from .models import Patient
from django.contrib.auth.models import User

class UserRegistrationTest(TestCase):
    def test_user_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'test@example.com'
        })
        self.assertEqual(response.status_code, 201)

class PatientModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.patient = Patient.objects.create(
            user=self.user,
            full_name="John Doe",
            gender="Male",
            phone_number="1234567890",
            date_of_birth="1990-01-01",
            address="123 Main St"
        )

    def test_patient_age(self):
        self.assertEqual(self.patient.age(), 35)