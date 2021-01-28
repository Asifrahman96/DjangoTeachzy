from django.urls import path,include
from . import views


app_name = 'teachers'

urlpatterns = [
    path('',views.teachers, name="teachers"),
    path('<int:id>',views.teacher, name="single"),
    path('search',views.search, name="search"),
    path('add_teacher',views.add_teacher, name="add_teacher"),
]