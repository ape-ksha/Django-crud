from django.test import TestCase, Client
from django.urls import reverse
from .models import Shop, User
import json


# Model Tests
class ModelTests(TestCase):
   

   def setUp(self):
        self.client = Client()
        self.home_page_url = reverse('view')
        self.shop1 = Shop.objects.create(
            name='shop1',
            latitude='0.788',
            longitude='-8.9000',
            address='electronic city'
        )
        self.add_shops_url = reverse('add')
        self.add_users_url = reverse('adduser')
        self.shop1 = Shop.objects.create(name='shop1',
           latitude='0.788',
           longitude='-8.9000',
          address='electronic city')
   

   def test_view_get(self):
     response = self.client.get(self.home_page_url)
     self.assertEquals(response.status_code, 200)
     self.assertTemplateUsed(response, 'mainapp/view.html')

   def test_add_post_add_new_shops(self):

     data = {'name':'shop1','latitude':0.788, 'longitude':-8.9000, 'address':'electronic city'}
     shop = Shop.objects.create(**data)
     response = self.client.post(self.add_shops_url, data=shop.__dict__)
     self.assertEqual(response.status_code, 200)
     self.assertTemplateUsed(response, 'success')


   def test_add_post_add_new_users(self):
      data = {'name':'user1','latitude':0.788, 'longitude':-8.9000, 'distance':1}
      user = User.objects.create(**data)
      response = self.client.post(self.add_users_url, data=user.__dict__)
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'mainapp/shops_within_distance.html')



