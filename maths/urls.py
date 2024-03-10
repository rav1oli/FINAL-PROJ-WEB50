#urls here
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.createProblem, name="create_problem"),

    #api routes
    path("sets/my_sets/<str:order>", views.my_sets, name="my_sets"), 
    path("sets/public/<str:order>", views.public_sets, name="public_sets"),
]