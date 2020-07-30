from django.test import TestCase
from django.urls import resolve, reverse
from reconocimientos.views import (dashboard, empleados, index, perfil,)


class TestUrls(TestCase):

    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_perfil_url_resolves(self):
        url = reverse('perfil', args=[1, ])
        self.assertEqual(resolve(url).func, perfil)

    def test_dashboard_url_resolves(self):
        url = reverse('dashboard')
        self.assertEqual(resolve(url).func, dashboard)

    def test_empleados_url_resolves(self):
        url = reverse('empleados')
        self.assertEqual(resolve(url).func, empleados)
