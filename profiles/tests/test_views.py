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


class TestLoginView(TestCase):

    def setUp(self):
        self.user = sample_user()

    def test_loginv(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    # def test_correct_registro(self):
    #     response = self.client.post('/login/', {
    #         'email': 'carlosjimenez@bluetab.net',
    #         'username': 'carlos',
    #         'password': '123pass'
    #         })
    #     self.assertTrue(response.content['authenticated'])
