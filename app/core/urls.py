from django.urls import path
from core import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('search/', views.search_account, name='search-account'),
    path('add-account/', views.add_account_to_process, name='add-account'),
    path('clear/', views.clear, name='clear'),
    path('create-account/', views.create_account, name='create-account'),
    path('accounts/<slug:client_id_slug>', views.account_detail, name='account-detail'),
    path('done-package/<int:package_id>/', views.done_package, name='done-package'),
]
