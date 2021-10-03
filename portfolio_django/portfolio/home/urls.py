from django.urls import path

from .views import (IndexTemplateView, ProjetoCreateView,
                    ProjetoDetailTemplateView)

app_name = 'home'

urlpatterns = [

    # Get HOME PAGE -> /
    path(
        '',
        IndexTemplateView.as_view(),
        name ='index'
    ),

    ## Utilizando o ID para buscar o projeto
    path(
        'video/projeto/<pk>',
        ProjetoDetailTemplateView.as_view(),
        name = 'projetos_detail'
    ),

    ## Criar um novo projeto
    path(
        'projeto/new/',
        ProjetoCreateView.as_view(),
        name = 'adicionar_projeto'
    ),
]
