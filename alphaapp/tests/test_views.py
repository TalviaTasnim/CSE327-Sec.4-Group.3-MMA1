from alphaapp.views import log, main
from alphaapp.models import Customer,Seller,User
from django.http import response
from django.test import TestCase, client
import json
from unittest import skip
from django.urls import reverse
# from django.contrib.auth.models import User
# from alphaapp.models import User,Customer,Seller
from django.test import client
import socket
socket.socket()



class TestViewResponse(TestCase):
    def setUp(self):
        self.customer_log_url=reverse('log')
        self.seller_log_url=reverse('log2')
        self.user_log_url=reverse('user-profile')

    def test_cutomer_log_GET(self):
        response=self.client.get(self.customer_log_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'login.html')

    def test_seller_log_GET(self):
        response=self.client.get(self.seller_log_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'login.html')

    def test_User_Profile_GET(self):
        response=self.client.get(self.user_log_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'userprofile.html')