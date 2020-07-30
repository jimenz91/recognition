from django.contrib.auth import get_user_model
from django.test import TestCase


def sample_user(email='carlosjimenez@bluetab.net', username='carlos',
                password='123pass'):
    """
    Método para crear un usuario para las pruebas.
    """
    return get_user_model().objects.create_user(email, username, password)


def sample_user_2(
        email='andresgomez@bluetab.net',
        username='andres',
        password='123pass'
        ):
    """
    Método para crear un usuario para las pruebas.
    """
    return get_user_model().objects.create_user(email, username, password)


class TestIndexView(TestCase):
    def test_index(self):
        resp = self.client.get('//')
        self.assertEqual(resp.status_code, 200)
