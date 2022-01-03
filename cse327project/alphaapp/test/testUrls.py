from django import urls
from django.test import SimpleTestCase
from django.urls import reverse
from django.urls import reverse, resolve
from alphaapp.views import contact,faq

class TestUrls(SimpleTestCase):


    def test_urls_contact_resolve(self):
        url=reverse('contact')
        print(resolve(url))
        self.assertEquals(resolve(url).func, contact)


    def test_urls_faq_resolve(self):
        url=reverse('faq')
        print(resolve(url))
        self.assertEquals(resolve(url).func, faq) 