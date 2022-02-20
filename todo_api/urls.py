
from django.urls import path, include
from rest_framework import routers
from . import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register("todoapi", views.TodosViewset, basename="todo")
urlpatterns = [
    path("", include(router.urls))
]
