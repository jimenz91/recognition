from profiles.models import User
from reconocimientos.models import Mencion
from django.shortcuts import get_object_or_404
from django.db.models import Avg


def AverageMentions(get_response):
    """
    Método para calcular el promedio de todas las menciones de todos
    los usuarios y actualizar el campo de promedio.
    Permite la actualización del ranking para mostrarlo en el índice.
    """
    def middleware(request):
        response = get_response(request)
        # Obtengo el número total de empleados registrados.
        n_empleados = User.objects.count()
        i = 1
        # Se realiza el bucle mientras por cada empleado registrado.
        while (i <= n_empleados):
            # Se calcula el promedio de todas las menciones en la base de datos
            # para cada usuario.
            promedio_total = Mencion.objects.filter(receptor=i).aggregate(Avg(
                'puntuacion__valor'
            ))
            empleado = get_object_or_404(User, pk=i)
            # Se actualiza el promedio del usuario en la BBDD.
            empleado.promedio_puntuaciones = promedio_total[
                'puntuacion__valor__avg'
            ]
            empleado.save()
            i += 1
        print('Promedios actualizados')
        return response
    return middleware
