from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('agenda.urls')),
    path('pacientes/', include('pacientes.urls')),
    path('usuarios/', include('usuarios.urls')),  # 👈 novo
]