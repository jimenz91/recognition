from django.contrib import admin
from reconocimientos.models import Categoria, Mencion, Proyecto, Puntuacion


class PuntuacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'denominacion', 'valor')
    list_display_links = ('denominacion',)


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre',)
    list_display_links = ('nombre',)

    # def get_empleados(self, obj):
    #     return "\n".join([e.nombre+' '+e.apellido for
    # e in obj.empleados.all()])


class MencionAdmin(admin.ModelAdmin):
    list_display = ('id', 'emisor', 'receptor',
                    'categoria', 'puntuacion', 'fecha_realización')
    list_filter = ('receptor',)
    list_display_links = ('id',)
    list_per_page = 20


class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'codigo', 'dificultad', 'autor')
    list_display_links = ('nombre',)


admin.site.register(Puntuacion, PuntuacionAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Mencion, MencionAdmin)
admin.site.register(Proyecto, ProyectoAdmin)
