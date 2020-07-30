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


class TestUserModel(TestCase):

    def test_create_user_with_email_successful(self):
        """Prueba de crear un nuevo usuario con el correo es exitoso."""
        email = 'jimenz91@gmail.com'
        username = 'jimenz'
        password = '123pass'
        nombre = 'carlos'
        apellido = 'Jiménez'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            username=username,
            first_name=nombre,
            last_name=apellido,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertEqual(user.first_name, nombre)
        self.assertEqual(user.last_name, apellido)
        self.assertEqual(user.username, username)

    def test_new_user_email_normalized(self):
        """Se asegura que el correo de un nuevo usuario está normalizado."""
        email = 'test@GMAil.com'
        user = get_user_model().objects.create_user(
                                                    email=email,
                                                    password='test123',
                                                    username='usuario'
                                                    )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Probar que crear un usuario sin un correo genera un error."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123', 'usuario')

    def test_create_new_superuser(self):
        """Se prueba la creación de un nuevo superusuario."""
        email = 'jimenz91@gmail.com'
        username = 'jimenz'
        password = '123pass'
        nombre = 'Carlos'
        apellido = 'Jiménez'

        user = get_user_model().objects.create_superuser(
            email=email,
            password=password,
            username=username,
            first_name=nombre,
            last_name=apellido,
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_user_str(self):
        """Se prueba la representación de los usuarios."""

        usuario = get_user_model().objects.create(
            email='carlosjimenez@bluetab.net',
            password='123pass',
            username='carlos',
            first_name='Carlos',
            last_name='Jiménez'
        )

        self.assertEqual(
            str(usuario),
            usuario.first_name+" "+usuario.last_name
            )
