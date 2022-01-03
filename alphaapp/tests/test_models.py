from django.contrib.auth.models import User
from alphaapp.models import User,Customer,Seller
from django.test import client
from django.test import TestCase, client

class TestModel(TestCase):

    def setUp(self):
          self.cutomer1=Customer.objects.create(
              first_name='mdfaisal',
              last_name='ahmed',
              email='mdfaisal@gmail.com' 
          )

          self.seller1=Seller.objects.create(
              first_name='mdfaisal',
              last_name='ahmed',
              email='mdfaisal@gmail.com' 
          )

    def Cutomer_attribute_creation(self):
        self.assertEquals(self.cutomer1.first_name, 'cutomer1')
        self.assertEquals(self.cutomer1.last_name, 'cutomer1')
        self.assertEquals(self.cutomer1.email, 'cutomer1')

    def Seller_attribute_creation(self):
        self.assertEquals(self.seller1.first_name, 'seller1')
        self.assertEquals(self.seller1.last_name, 'seller1')
        self.assertEquals(self.seller1.email, 'seller1')