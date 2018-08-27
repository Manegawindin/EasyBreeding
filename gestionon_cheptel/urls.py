from django.urls import path
from gestionon_cheptel.views import views


app_name = 'gestionon_cheptel'

urlpatterns=[
    path('', views.index2, name='index2'),
    path('gestion', views.IndexView.as_view(), name='accueil'),
    path('creer/cheptel', views.creerCheptel, name='creerCheptel'),
    path('evenement/creer', views.CreerEvenement, name='creerEvenement'),
]