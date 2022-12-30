from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('admin/', admin.site.urls),
   path('tablica_ogloszen/', include('tablica_ogloszen.urls', namespace='tablica_ogloszen')),
]

