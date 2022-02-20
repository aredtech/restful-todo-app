from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Todo

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import FormView

# Create your views here.
class CustomizedLoginView(LoginView):
    template_name = "todo/login.html"
    redirect_authenticated_user = True
    fields = "__all__"
    def get_success_url(self):
        return reverse_lazy("index")

class CustomizedRegisterView(FormView):
    template_name = "todo/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class IndexView(LoginRequiredMixin, ListView):
    template_name = "todo/index.html"
    model = Todo
    context_object_name = "todos"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todos"] = context["todos"].filter(user=self.request.user)
        return context


class TodoDetailView(LoginRequiredMixin, DetailView):
    template_name = "todo/todo_detail.html"
    model = Todo
    context_object_name = "todo"


class TodoCreatView(LoginRequiredMixin, CreateView):
    template_name = "todo/todo_create.html"
    model = Todo
    fields = ["title", "description", "complete"]
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TodoUpdate(LoginRequiredMixin, UpdateView):
    template_name = "todo/todo_update.html"
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("index")

class TodoDelete(LoginRequiredMixin, DeleteView):
    template_name = "todo/todo_delete.html"
    model = Todo
    success_url = reverse_lazy("index")
    context_object_name = "todo"

