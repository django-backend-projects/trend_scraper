from django.urls import path
from . import views


urlpatterns = [
    path('declarations/', views.DeclarationListApiView.as_view(), name='declarations'),
]