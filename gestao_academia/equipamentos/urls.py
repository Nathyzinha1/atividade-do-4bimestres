from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categorias/', views.categoria_list, name='categoria_list'),
    path('categorias/nova/', views.categoria_create, name='categoria_create'),
    path('categorias/<int:pk>/', views.categoria_detail, name='categoria_detail'),
    path('categorias/<int:pk>/editar/', views.categoria_update, name='categoria_update'),
    path('categorias/<int:pk>/excluir/', views.categoria_delete, name='categoria_delete'),
    path('equipamentos/', views.equipamento_list, name='equipamento_list'),
    path('equipamentos/novo/', views.equipamento_create, name='equipamento_create'),
    path('equipamentos/<int:pk>/', views.equipamento_detail, name='equipamento_detail'),
    path('equipamentos/<int:pk>/editar/', views.equipamento_update, name='equipamento_update'),
    path('equipamentos/<int:pk>/excluir/', views.equipamento_delete, name='equipamento_delete'),
]
