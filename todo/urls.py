from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", views.CustomizedRegisterView.as_view(), name="register"),
    path("login/", views.CustomizedLoginView.as_view(), name="login"),
    path("create-todo/", views.TodoCreatView.as_view(), name="todo-create"),
    path("todos/<int:pk>/", views.TodoDetailView.as_view(), name="todo-detail"),
    path("update-todo/<int:pk>", views.TodoUpdate.as_view(), name="todo-update"),
    path("delete-todo/<int:pk>", views.TodoDelete.as_view(), name="todo-delete"),
]
