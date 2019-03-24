from django.test import TestCase
from .models import Teamlist
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class ModelTestCase(TestCase):
    """This class defines the test suite for the Teamlist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.teamlist_name = "wekesa"
        self.teamlist_specialty = "django"
        self.teamlist = Teamlist(name=self.teamlist_name, specialty=self.teamlist_specialty)

    def test_model_can_create_a_teamlist(self):
        """Test the teamlist model can create a teamlist."""
        initial_team_count = Teamlist.objects.count()
        self.teamlist.save()
        new_team_count = Teamlist.objects.count()
        self.assertNotEqual(initial_team_count, new_team_count)

class ViewTestCase(TestCase):
    """This class defines the test suite for the Teamlist views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.teamlist_data = {
                'name':'wepundi',
                'specialty':'python flask'
            }
        self.response = self.client.post(
            reverse('create'),
            self.teamlist_data,
            format="json"
        )

    def test_api_can_create_a_teamlistlist(self):
        """Test the api has teamlist creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

