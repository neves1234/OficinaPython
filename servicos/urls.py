from django.urls import path
from . import views
from .views import finalizar_servico

urlpatterns = [
   path('novo_servico/', views.novo_servico, name="novo_servico"),
   path('listar_servico/', views.listar_servico, name="listar_servico"),
   path('servico/<str:servico_id>/', views.servico, name="servico"),
   path('finalizar_servico/<int:servico_id>/', finalizar_servico, name='finalizar_servico'),

]