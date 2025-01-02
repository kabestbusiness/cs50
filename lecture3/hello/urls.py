from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name = 'index'),
    path("james", views.james, name = 'james'),
    path('<str:name>', views.greet, name = 'greet')
]