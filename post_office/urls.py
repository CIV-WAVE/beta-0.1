from django.urls import path
from django.contrib.auth import views as auth_views

from post_office import views

app_name = 'post_office'

urlpatterns = [
    path('',
         views.home,
         name='home'),

    path('logout/',
         auth_views.LogoutView.as_view(),
         name='departure'),

    path('passport_application/',
         views.passport_application,
         name='passport_application'),

    path('passports',
         views.passport_list,
         name='passport_list'),

    path('passports/<slug:slug>',
         views.PassportDetailView.as_view(),
         name='passport_detail'),
]
