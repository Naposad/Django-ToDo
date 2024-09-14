from django.urls import path, include
from .views import Accueil

urlpatterns = [
    path('accounts/', include('allauth.urls')),  # Allauth URL patterns
    path('', include('todoListe.urls')),
    path('', Accueil.as_view(), name='accueil'),
]