
from django.urls import path
from . import views # . significa que importa desde el mismo directorio


urlpatterns = [
    path('',views.home, name ='home'),
    path('/createNPC', views.createNPC),
    path('/NPCGenerator', views.createNPC, name="NPCGenerator"),
]
