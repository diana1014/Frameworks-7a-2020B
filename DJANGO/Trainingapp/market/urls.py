from django.urls import path
from.import views

urlpatterns=[

    path('index', views.index, name='index'),
    path('listar_categorias', views.listar_categorias, name='listar_categorias')
]

