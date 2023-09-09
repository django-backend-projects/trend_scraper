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

    # upload excell file
    path('upload-excell-asan-login/', views.upload_asan_excell, name='upload-excell-asan-login'),
    path('upload-excell-user-info', views.upload_user_id_and_shipingId, name='upload-excell-user-info'),

    # process excell data
    path('process-excell-user-info/', views.process_excell_user_info, name='process-excell-user-info'),
    path('process-excell-decl-info/', views.process_excell_decl_info, name='process-excell-decl-info'),

    # press button to process 
    path('process/', views.process_daclaration, name='process-declaration'),
]
