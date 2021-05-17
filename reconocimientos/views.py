import datetime as dt
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models import Avg, F
from django.shortcuts import get_object_or_404, redirect, render
from .choices import categorias, puntuaciones, proyectos
from .models import Mencion
import pandas as pd
import plotly.express as px
from plotly.offline import plot

User = get_user_model()
today = dt.datetime.now()


def grafico_radar(menciones):
    """Método para graficar el promedio de mensiones de un usuario."""

    categorias = list(menciones.keys())
    promedios = list(menciones.values())

    df = pd.DataFrame(dict(
        r=promedios,
        theta=categorias))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True,
                        range_r=[0, 100]
                        )
    plot_div = plot(fig, output_type='div', config={'displayModeBar': False})

    return plot_div


def promedio_por_categorias(empleado, pk, menciones):
    """
    Método para calcular el promedio de las menciones recibidas por un
    usuario, dividido por categoría para mostrarlas en su gráfico de radar.
    """
    agregado = 0
    # Se obtienen todas las categorías asignadas al usuario y se recorren una
    # por una. Se crea una lista con todas las menciones y se devuelve
    # la lista.
    for categoria in empleado.categorias.all():
        id_categoria = categoria.id
        promedio_cat = Mencion.objects.filter(
            receptor=pk,
            categoria=id_categoria
        ).aggregate(Avg('puntuacion__valor'))
        menciones[categoria.nombre] = promedio_cat['puntuacion__valor__avg']
        if promedio_cat['puntuacion__valor__avg']:
            agregado = agregado + menciones[categoria.nombre]
    return menciones


def crear_menciones(request, pk, empleado):
    """
    Método para crear menciones nuevas para los usuarios, recibiendo las
    puntuaciones que se quieren aceptar y el empleado receptor.
    """
    # Obtengo la id del usuario y sus categorías
    user_id = request.user.id
    categorias_empleado = empleado.categorias.all()

    menciones_creadas = []

    for campo in categorias_empleado:
        # Obtengo la puntuación del formulario.
        puntuacion = request.POST[campo.nombre]
        categoria = categorias[campo.nombre]
        puntuacion_id = puntuaciones[puntuacion]
        # Se crea la nueva mención en la base de datos.
        mencion = Mencion(emisor_id=user_id, categoria_id=categoria,
                          puntuacion_id=puntuacion_id, receptor_id=pk
                          )
        mencion.save()
        # Se llena la lista de nuevas menciones en cada iteración del bucle.
        menciones_creadas.append(mencion)
    return menciones_creadas


def index(request):
    """
    Vista principal de la web, con el listado de los usuarios con mayor
    promedio de puntuaciones.
    """
    # Se muestran todos los empleados activos, con proyectos asignados y con
    # menciones recibidas, ordenados de mayor a menor por el promedio.
    empleados = User.objects.order_by('-promedio_puntuaciones').filter(
        is_active=True,
        proyectos__isnull=False,
        promedio_puntuaciones__isnull=False
    ).exclude(first_name='Admin')[:10]

    context = {
        'empleados': empleados,
    }

    return render(request, 'index.html', context)


def perfil(request, pk):
    """
    View para ver el perfil de otros usuarios, así como la asignación de
    menciones.
    """

    empleado = get_object_or_404(User, pk=pk)
    menciones = {}
    compañeros = False
    if request.user.is_authenticated:
        usuario = User.objects.get(pk=request.user.id)
        proyectos_usuario = usuario.proyectos.all()
        proyectos_empleado = empleado.proyectos.all()

        # Se comprueba si el empleado del perfil y el usuario logado son
        # compañeros de proyecto.
        for pe in proyectos_empleado:
            for pu in proyectos_usuario:
                if pe == pu:
                    compañeros = True
                else:
                    compañeros = False
    # Se revisa si el usuario ha recibido menciones.
    if Mencion.objects.filter(receptor=pk):
        # Si ha recibido menciones, se calcula el promedio por categorías para
        # maquetar el gráfico de radar.
        menciones = promedio_por_categorias(empleado, pk, menciones)

        if request.method == 'POST':
            # Se revisa si el usuario está logado:
            if request.user.is_authenticated:
                # Se confirma que el empleado del perfil y el usuario logado
                # sean compañeros de algún proyecto.
                if compañeros is True:
                    # Se revisa el número de menciones disponibles
                    if request.user.menciones_hechas > 0:
                        # Se confirma si existen menciones hechas por el
                        # usuario en el mes en curso.
                        if Mencion.objects.filter(
                                receptor=pk,
                                fecha_realización__month=today.month
                        ):
                            messages.error(
                                request, 'Ya ha creado una mención \
                                    para este usuario en este mes.'
                            )

                            return redirect('perfil', pk)
                        else:
                            # Se crea la nueva mención, se le resta una a las
                            # menciones disponibles del usuario emisor.
                            crear_menciones(request, pk, empleado)
                            usuario.menciones_hechas = F(
                                'menciones_hechas') - 1
                            usuario.save()
                            messages.success(
                                request, 'Mención realizada correctamente.'
                            )
                            print("Mención realizada correctamente.")
                            return redirect('perfil', pk)
                    else:
                        messages.error(
                            request, 'Imposible crear mención ya que has \
                                utilizado todas las de este mes.'
                        )
                        return redirect('perfil', pk)
                else:
                    print("No son compañeros.")
    else:
        # Si el usuario no tiene menciones, no se hace nada.
        if request.method == 'POST':
            if request.user.is_authenticated:
                # Se confirma que el empleado del perfil y el usuario logado
                # sean compañeros de algún proyecto.
                if compañeros is True:
                    # Se revisa el número de menciones disponibles
                    if request.user.menciones_hechas > 0:
                        crear_menciones(request, pk, empleado)
                        usuario.menciones_hechas = F('menciones_hechas') - 1
                        usuario.save()
                        messages.success(
                            request, 'Mención realizada correctamente.'
                        )
                        return redirect('perfil', pk)
                    else:
                        messages.error(
                            request, 'No tienes menciones disponibles.'
                        )
                        return redirect('perfil', pk)

    # Se maqueta el radar del usuario.
    plot_div = grafico_radar(menciones)

    context = {
        'empleado': empleado,
        'menciones': menciones,
        'plot_div': plot_div,
        'compañeros': compañeros
    }

    return render(request, 'perfil.html', context)


def dashboard(request):
    """
    View para el dashboard del usuario logado.
    """

    # Se obtiene el objeto del usuario logado:
    usuario = request.user
    menciones = {}
    # Se obtienen los promedios de las menciones por categoria del usuario.
    menciones = promedio_por_categorias(usuario, usuario.id, menciones)

    # Se maqueta el radar del usuario.
    plot_div = grafico_radar(menciones)

    # Se obtienen todos los empleados menos el usuario y el admin.
    empleados = User.objects.exclude(pk__in=[usuario.id, 1])

    # Se obtienen todos los proyectos del usuario logado.
    proyectos_usuario = usuario.proyectos.all()

    compañeros = []

    # Se comparan los proyectos del usuario con los proyectos de cada uno de
    # los empleados para determinar qué usuarios son sus compañeros y armar
    # una lista con ellos.
    for pu in proyectos_usuario:
        for e in empleados:
            if pu in e.proyectos.all():
                compañeros.append(e)

    ultimas_menciones = Mencion.objects.filter(
        emisor=usuario.id,).order_by('-fecha_realización')[:5]

    context = {
        'menciones': menciones,
        'plot_div': plot_div,
        'compañeros': compañeros,
        'ultimas_menciones': ultimas_menciones
    }

    return render(request, 'dashboard.html', context)


def empleados(request):
    """
    View que contiene un listado con todos los empleados y permite filtrar por
    nombre, apellido, categorías y proyectos.
    """

    # Se obtiene al usuario logado
    usuario = request.user

    # Se obtienen todos los usuarios, menos el que está logado y
    # el administrador.
    empleados = User.objects.exclude(pk__in=[usuario.id, 1])

    # Se revisan los diferentes campos del formulario de búsqueda para realizar
    # la query con los parámetros introducidos.
    if 'nombre' in request.GET:
        nombre = request.GET['nombre']
        if nombre:
            empleados = empleados.filter(first_name__icontains=nombre)

    if 'apellido' in request.GET:
        apellido = request.GET['apellido']
        if apellido:
            empleados = empleados.filter(last_name__icontains=apellido)

    if 'categorias' in request.GET:
        categoria = request.GET['categorias']
        if categoria:
            empleados = empleados.filter(categorias__nombre__in=[categoria])

    if 'proyectos' in request.GET:
        proyecto = request.GET['proyectos']
        if proyecto:
            empleados = empleados.filter(proyectos__nombre__in=[proyecto])

    context = {
        'values': request.GET,
        'proyectos': proyectos,
        'categorias': categorias,
        'empleados': empleados
    }

    return render(request, 'empleados.html', context)
