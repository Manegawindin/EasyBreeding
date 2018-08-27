"""EasyBreeding2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import  url
from django.conf import settings
from gestionon_cheptel.views import views
from django.contrib.auth import views as auth_views
from . import views

# from . import viewes

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('cheptel/', include('gestionon_cheptel.urls')),
    #path('accounts/', include('registration.auth_urls')),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name='user/pass_reset.html', email_template_name='user/pass_reset_email.html', subject_template_name='user/email_subject.txt' ), name='password_reset'),
    path('accounts/logout', auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),
    path('accounts/password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='user/pass_reset_done.html'), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user/pass_reset_confirm.html'), name='password_confirm' ),
    path('accounts/reset_complet/', auth_views.PasswordResetCompleteView.as_view(template_name='user/pass_reset_complet.html'), name='password_reset_complete'  ),
    path('accounts/create/', views.UserCreationView, name='create_user'),
    url('accounts/activate/<uidb64>/<token>/', views.activate, name='activate'),
]

if settings.DEBUG:

    import debug_toolbar

    urlpatterns = [

        url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns