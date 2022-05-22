from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.userpage, name='userpage'),
    path('<int:pk>/update', views.UserUpdate, name='update')

]