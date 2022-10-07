from django.urls import path

from . import views

urlpatterns = [
    path('rooms', views.rooms, name='rooms'),
    path('<int:id>', views.detail, name='detail'),
    path('new', views.new, name='new')
]