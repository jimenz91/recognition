from django.contrib import admin
from profiles.models import User


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'is_active', 'promedio_puntuaciones',
                    'menciones_hechas', 'get_proyectos', 'get_categorias')
    list_editable = ('is_active',)
    list_display_links = ('id', 'username')

    def get_categorias(self, obj):
        return "\n".join([c.nombre for c in obj.categorias.all()])

    # def get_menciones(self, obj):
    #     return "\n".join([m.categoria for m in obj.menciones.all()])

    def get_proyectos(self, obj):
        return "\n".join([p.nombre for p in obj.proyectos.all()])


admin.site.register(User, EmpleadoAdmin)
