from django import urls
from django.test import SimpleTestCase
from django.urls import reverse
from django.urls import reverse, resolve
from alphaapp.views import home,main,Signup,log,log2, UserProfile

class TestUrls(SimpleTestCase):


    def test_urls_home_resolve(self):
        url=reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)


    def test_urls_main_resolve(self):
        url=reverse('main')
        print(resolve(url))
        self.assertEquals(resolve(url).func, main)

    def test_urls_signUp_resolve(self):
        url=reverse('signup')
        print(resolve(url))
        self.assertEquals(resolve(url).func, Signup)

    def test_urls_log_resolve(self):
        url=reverse('log')
        print(resolve(url))
        self.assertEquals(resolve(url).func, log)   

    def test_urls_log2_resolve(self):
        url=reverse('log2')
        print(resolve(url))
        self.assertEquals(resolve(url).func, log2)

    def test_urls_UserPrfile_resolve(self):
        url=reverse('user-profile')
        print(resolve(url))
        self.assertEquals(resolve(url).func, UserProfile)  