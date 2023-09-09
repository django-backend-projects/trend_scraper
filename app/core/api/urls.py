from django.urls import path
from . import views


urlpatterns = [
    path('declarations/', views.DeclarationListApiView.as_view(), name='declarations'),
    path('create-declaration/', views.DeclarationCreateApiView.as_view(), name='create-declaration'),
]