from django.urls import path
from . import views

app_name = "tasks"
urlpatterns = [
    path("",views.energy,name="energy"),
    path("add/",views.add,name="add")
]
