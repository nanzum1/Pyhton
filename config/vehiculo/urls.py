from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_vehiculo, name='add'),
    path('', views.index, name='index'),
    path('list/', views.list_vehiculo, name='list'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]
