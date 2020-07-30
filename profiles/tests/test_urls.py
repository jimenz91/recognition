from django.test import TestCase
from django.urls import resolve, reverse
from profiles.views import (loginv, logoutv, registro,)


class TestUrls(TestCase):

    def test_login_url_resolves(self):
        url = reverse('loginv')
        self.assertEqual(resolve(url).func, loginv)

    def test_logout_url_resolves(self):
        url = reverse('logoutv')
        self.assertEqual(resolve(url).func, logoutv)

    def test_registro_url_resolves(self):
        url = reverse('registro')
        self.assertEqual(resolve(url).func, registro)
