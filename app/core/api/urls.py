from django.urls import path
from . import views


urlpatterns = [
    path('send-declarations/', views.ApplySmartCustomsView.as_view(), name='send-declarations'),
]
