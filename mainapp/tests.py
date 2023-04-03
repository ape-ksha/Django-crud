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
      #   self.update_url = reverse('view')
   def test_update_shop(self):
      #   updated_data = {'name':'shop1',
      #      'latitude':'0.788',
      #      'longitude':'-8.9000',
      #     'address':'ecoworld'}
      self.shop1.address='ecoworld'
      self.shop1.save()
      updated_obj = Shop.objects.get(pk=self.shop1.pk)
      self.assertEqual(updated_obj.address, 'ecoworld')
      #   response = self.client.post(self.home_page_url, data=updated_data)
      #   self.assertEqual(response.status_code, 302)
      #   self.shop1.refresh_from_db()
      #   self.assertEqual(self.shop1.address, 'ecoworld')

     
   

   def test_view_get(self):
     response = self.client.get(self.home_page_url)
     self.assertEquals(response.status_code, 200)
     self.assertTemplateUsed(response, 'mainapp/view.html')

   def test_add_post_add_new_shops(self):

     data = {'name':'shop1','latitude':0.788, 'longitude':-8.9000, 'address':'electronic city'}
     shop = Shop.objects.create(**data)
     response = self.client.post(self.add_shops_url, data=shop.__dict__)
     self.assertEqual(response.status_code, 200)


   def test_add_post_add_new_users(self):
      data = {'name':'user1','latitude':0.788, 'longitude':-8.9000, 'distance':1}
      user = User.objects.create(**data)
      response = self.client.post(self.add_users_url, data=user.__dict__)
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'mainapp/shops_within_distance.html')



   def test_delete(self):
        initial_count = Shop.objects.count()
     #    shop_delete = Shop.objects.get(pk=self.shop_delete.pk)
        self.shop1.delete()
        final_count = Shop.objects.count()
        self.assertEqual(initial_count - 1, final_count)
        self.assertFalse(Shop.objects.filter(name='shop1').exists())

