#urls here
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.createProblem, name="create_problem"),

    #api routes
    path("sets/public/<str:order>", views.problem_sets, name="public_sets"),
    path("sets/personal/<str:order>", views.problem_sets, name="personal_sets"),
    path("sets/<str:subset>/<str:order>", views.problem_sets, name="personal_sets"),
]