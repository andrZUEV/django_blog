from django.urls import path
from . import views

'''Свяжем view с именем post_list  с корневым URL-адресом(''), имена URL должны быть понятными и уникальными'''

urlpatterns = [
    path('', views.post_list, name = 'post_list'),
    path('post/<int:pk>/' , views.post_detail , name = 'post_detail'),
]