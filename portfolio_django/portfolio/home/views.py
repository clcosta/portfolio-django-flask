from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from portfolio.models import Projeto

from home.forms import ProjetoCreateForm


class IndexTemplateView(ListView):
    template_name = "home/index.html"
    model = Projeto
    fields = [
        'id',
        'titulo',
        'capa',
    ]
    context_object_name = "projetos"

class ProjetoDetailTemplateView(DetailView):
    template_name = 'home/projeto.html'
    model = Projeto
    fields = [
        'titulo',
        'iframe_video',
        'link_codigo',
    ]
    context_object_name = "projetos_detail"

class ProjetoCreateView(CreateView):
    template_name = 'home/adicionar_projeto.html'
    model = Projeto
    form_class = ProjetoCreateForm
    success_url = reverse_lazy(
        "home:index"
    )

def handle_not_found(request, exception):
    return render(request, '404.html')

def handle_server_error(request):
    return render(request, '500.html')

def handle_permission_denied(request, exception):
    return render(request, '403.html')

def handle_bad_request(request, exception):
    return render(request, '400.html')
