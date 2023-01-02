from django.contrib import admin
from django.urls import path, include

from Projekt_TO.views import home_view

urlpatterns = [
   path('', home_view),
   path('admin/', admin.site.urls),
   path('tablica_ogloszen/', include('tablica_ogloszen.urls', namespace='tablica_ogloszen')),
]

