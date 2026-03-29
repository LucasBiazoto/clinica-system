from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🔥 conecta o app agenda
    path('agenda/', include('agenda.urls')),
]