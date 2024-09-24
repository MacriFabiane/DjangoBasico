from django.urls import path
from . import views #importe views da propria pasta

urlpatterns = [#para urls filhas de blog
    path('', views.index)#nesse caso vazia ela vai referenciar a ela mesma
]