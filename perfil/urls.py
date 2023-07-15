from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('gerenciar', views.gerenciar),
    path('cadastrar_banco/', views.cadastrar_banco, name="cadastrar_banco"),
    path("remover_banco/<int:id>" , views.remover_banco , name =  "remover_banco"),
    path('cadastrar_categoria/', views.cadastrar_categoria, name="cadastrar_categoria"),
    path('alterar_essencial/<int:id>' , views.alterar_essencial, name = "alterar_essencial"),
    path('dashboard/' , views.dashboard , name = "dashboard")
]