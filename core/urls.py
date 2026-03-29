from django.contrib import admin
from django.urls import path, include
from core.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard, name="dashboard"),
    path('', include('usuarios.urls')),
    path('agenda/', include('agenda.urls')),
    path('financeiro/', include('financeiro.urls')),
]