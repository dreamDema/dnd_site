from django.urls import path

from . import  views

urlpatterns = [
    path('', views.index, name='HomePage'),
    # path('shot/<slug:name_game>/', views.index, name='HomePage'),
]
