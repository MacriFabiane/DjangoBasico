from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),#name deixa mais facil de referenciar a url
    path('sobre/', views.sobre, name='sobre'), #dentro do mesmo app outra page
]


