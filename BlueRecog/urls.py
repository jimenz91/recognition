from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reconocimientos.urls')),
    path('', include('profiles.urls')),
    path('api/', include('reconocimientos.api.urls')),
    path('api/', include('profiles.api.urls'))
]
