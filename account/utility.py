from os import path

from account import views

urlpattern = [
    path('accounts', views.list_account)
]