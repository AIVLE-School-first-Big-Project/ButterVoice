from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Homeapp'
urlpatterns = [
    path('role/', views.role, name='role'),
    path('home/', views.home, name='home'),
    path('home/<str:type>', views.home_type, name='home_type'),
    path('signin/', views.signin, name='signin'),
    path('logout/<str:type>', views.logout, name='logout'),
    path('uploadFile/', views.uploadFile, name='uploadFile'),
    path('signups/<str:type>', views.signups, name='signups'),
    path('signup/', views.signup, name='signup')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
