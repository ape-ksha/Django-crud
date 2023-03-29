from django.test import TestCase, Client
from django.urls import reverse
from .models import Shop, User
import json


# Model Tests
class ModelTests(TestCase):
   

   def setUp(self):
        self.client = Client()
        self.shops_list_url = reverse('')
   
   def test_view(self):
       response = self.client.get(self.shops_list_url)
       self.assertEquals(response.status_code, 200)
       self.assertTemplateUsed(response, 'view.html')
       