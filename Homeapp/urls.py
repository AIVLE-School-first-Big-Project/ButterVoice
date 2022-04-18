from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'Homeapp'

urlpatterns = [
    path('role/', views.role, name ='role'),
    path('home/', views.home, name ='home'),
    path('signin/', views.signin, name ='signin'),
    path('logout/', views.logout, name ='logout'),

    path('signups/<str:type>', views.signups, name ='signups'),
    path('signup/', views.signup, name ='signup'),
]