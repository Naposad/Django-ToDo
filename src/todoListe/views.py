from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, UpdateView, DetailView, ListView, DeleteView
from .models import TodoListe
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy


# Create your views here.

class CreateTodo(CreateView, LoginRequiredMixin):
    model = TodoListe
    template_name = 'todoListe/create-todo.html'
    success_url = reverse_lazy('todo-liste')
    fields = ['name', 'date_on', 'date_end', 'completed']

    def form_valid(self, form):
        form.instance.author = self.request.user
        print(self.request.user)
        return super().form_valid(form)


class ListeTodo(ListView, LoginRequiredMixin):
    model = TodoListe
    template_name = 'todoListe/liste-todo.html'
    success_url = reverse_lazy('todo-liste')
    context_object_name = 'todos'

    def get_queryset(self):
        queryset = TodoListe.objects.filter(author=self.request.user)
        return queryset


class UpdateTodo(UpdateView, LoginRequiredMixin):
    model = TodoListe
    template_name = 'todoListe/update-todo.html'
    success_url = reverse_lazy('todo-liste')
    fields = ['name', 'date_on', 'date_end', 'completed']



class DeleteTodo(DeleteView):
    model = TodoListe
    success_url = reverse_lazy('todo-liste')


class DetailTodo(DetailView):
    model = TodoListe
    template_name = 'todoListe/detail-todo.html'

