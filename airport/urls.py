from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'airport'

urlpatterns = [
    path('',
         views.home,
         name='home'),

    path('logout/',
         auth_views.LogoutView.as_view(),
         name='departure'),

    path('immigration/',
         auth_views.LoginView.as_view(template_name='airport/immigration.html'),
         name='immigration'),
]
