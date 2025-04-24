from django.urls import path
from . import views

urlpatterns = [
    path('transactions/add/', views.transaction_create, name='transaction_create'),
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('transactions/<int:transaction_id>/edit/', views.transaction_edit, name='transaction_edit'),
    path('transactions/<int:transaction_id>/delete/', views.transaction_delete, name='transaction_delete'),
    path('statuses/add/', views.status_create, name='status_create'),
    path('statuses/<int:status_id>/edit/', views.status_edit, name='status_edit'),
    path('statuses/<int:status_id>/delete/', views.status_delete, name='status_delete'),
    path('types/add/', views.type_create, name='type_create'),
    path('types/<int:type_id>/edit/', views.type_edit, name='type_edit'),
    path('types/<int:type_id>/delete/', views.type_delete, name='type_delete'),
    path('categories/add/', views.category_create, name='category_create'),
    path('categories/<int:category_id>/edit/', views.category_edit, name='category_edit'),
    path('categories/<int:category_id>/delete/', views.category_delete, name='category_delete'),
    path('subcategories/add/', views.subcategory_create, name='subcategory_create'),
    path('subcategories/<int:subcategory_id>/edit/', views.subcategory_edit, name='subcategory_edit'),
    path('subcategories/<int:subcategory_id>/delete/', views.subcategory_delete, name='subcategory_delete'),
    path('references/', views.reference_list, name='reference_list'),
    path('', views.home, name='home'),
]