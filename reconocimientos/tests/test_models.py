from django.contrib.auth import get_user_model
from django.test import TestCase

from reconocimientos.models import Categoria, Mencion, Proyecto, Puntuacion


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


class TestCategoriaModel(TestCase):

    def test_create_categoria(self):
        """Se prueba la creación de una nueva categoría"""

        nombre = 'Soft Skills',
        descripcion = 'Es una categoría'

        categoria = Categoria.objects.create(
            nombre=nombre,
            descripcion=descripcion
        )

        self.assertEqual(categoria.nombre, nombre)
        self.assertEqual(categoria.descripcion, descripcion)

    def test_categoria_str(self):
        """Se prueba la representación de las categorías."""
        categoria = Categoria.objects.create(
            nombre='Soft Skills'
        )

        self.assertEqual(str(categoria), categoria.nombre)


class TestPuntuacionModel(TestCase):

    def test_create_puntuacion(self):
        """Prueba la creación de una nueva puntuación."""
        denomincacion = 'F'
        valor = 0
        descripcion = 'La peor puntuación posible.'

        puntuacion = Puntuacion.objects.create(
            denominacion=denomincacion,
            valor=valor,
            descripcion=descripcion
        )

        self.assertEqual(puntuacion.denominacion, denomincacion)
        self.assertEqual(puntuacion.valor, valor)
        self.assertEqual(puntuacion.descripcion, descripcion)

    def test_puntuacion_verbose_name(self):
        """Se prueba el nombre en plural del modelo."""
        self.assertEqual(
            str(Puntuacion._meta.verbose_name_plural),
            'Puntuaciones')

    def test_puntuacion_str(self):
        """Se prueba la representación de las puntuaciones."""
        puntuacion = Puntuacion.objects.create(
            denominacion='G',
            valor=0
        )

        self.assertEqual(str(puntuacion), puntuacion.denominacion)


class TestProyectoModel(TestCase):

    def test_create_proyecto(self):
        """Se prueba la creación de un nuevo proyecto"""
        nombre = 'Web'
        descripcion = 'Páginas web.'
        codigo = 'BT25'
        dificultad = 10
        autor = sample_user()

        proyecto = Proyecto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            codigo=codigo,
            dificultad=dificultad,
            autor=autor
        )

        self.assertEqual(proyecto.nombre, nombre)
        self.assertEqual(proyecto.descripcion, descripcion)
        self.assertEqual(proyecto.codigo, codigo)
        self.assertEqual(proyecto.dificultad, dificultad)

    def test_proyecto_str(self):
        """Se prueba la representación del nombre del proyecto."""

        proyecto = Proyecto.objects.create(
            nombre='Machine Learning',
            dificultad=10
        )

        self.assertEqual(str(proyecto), proyecto.nombre)


class TestMencionModel(TestCase):

    def test_create_mencion(self):
        """Se prueba la creación de nuevas menciones."""
        emisor = sample_user()
        receptor = sample_user_2()
        categoria = Categoria.objects.create(nombre='Soft Skills')
        puntuacion = Puntuacion.objects.create(
            denominacion='F',
            valor=0,
            descripcion='La peor puntuacion.'
        )

        mencion = Mencion.objects.create(
            emisor=emisor,
            receptor=receptor,
            categoria=categoria,
            puntuacion=puntuacion
        )

        self.assertEqual(mencion.emisor, emisor)
        self.assertEqual(mencion.receptor, receptor)
        self.assertEqual(mencion.categoria, categoria)
        self.assertEqual(mencion.puntuacion, puntuacion)

    def test_menciones_verbose_name(self):
        """Se prueba el nombre en plural del modelo."""
        self.assertEqual(str(Mencion._meta.verbose_name_plural), 'Menciones')
