from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .api_views import (
    TransactionViewSet, StatusViewSet, TypeViewSet,
    CategoryViewSet, SubCategoryViewSet
)

router = DefaultRouter()
router.register(r'api/transactions', TransactionViewSet)
router.register(r'api/statuses', StatusViewSet)
router.register(r'api/types', TypeViewSet)
router.register(r'api/categories', CategoryViewSet)
router.register(r'api/subcategories', SubCategoryViewSet)

urlpatterns = [
    # URL для создания новой транзакции
    path('transactions/add/', views.transaction_create, name='transaction_create'),

    # URL для отображения списка всех транзакций
    path('transactions/', views.transaction_list, name='transaction_list'),

    # URL для редактирования существующей транзакции
    path('transactions/<int:transaction_id>/edit/', views.transaction_edit, name='transaction_edit'),

    # URL для удаления транзакции
    path('transactions/<int:transaction_id>/delete/', views.transaction_delete, name='transaction_delete'),

    # URL для создания нового статуса
    path('statuses/add/', views.status_create, name='status_create'),

    # URL для редактирования существующего статуса
    path('statuses/<int:status_id>/edit/', views.status_edit, name='status_edit'),

    # URL для удаления статуса
    path('statuses/<int:status_id>/delete/', views.status_delete, name='status_delete'),

    # URL для создания нового типа транзакции
    path('types/add/', views.type_create, name='type_create'),

    # URL для редактирования существующего типа транзакции
    path('types/<int:type_id>/edit/', views.type_edit, name='type_edit'),

    # URL для удаления типа транзакции
    path('types/<int:type_id>/delete/', views.type_delete, name='type_delete'),

    # URL для создания новой категории
    path('categories/add/', views.category_create, name='category_create'),

    # URL для редактирования существующей категории
    path('categories/<int:category_id>/edit/', views.category_edit, name='category_edit'),

    # URL для удаления категории
    path('categories/<int:category_id>/delete/', views.category_delete, name='category_delete'),

    # URL для создания новой подкатегории
    path('subcategories/add/', views.subcategory_create, name='subcategory_create'),

    # URL для редактирования существующей подкатегории
    path('subcategories/<int:subcategory_id>/edit/', views.subcategory_edit, name='subcategory_edit'),

    # URL для удаления подкатегории
    path('subcategories/<int:subcategory_id>/delete/', views.subcategory_delete, name='subcategory_delete'),

    # URL для отображения списка справочных данных (статусы, типы, категории, подкатегории)
    path('references/', views.reference_list, name='reference_list'),

    # URL для главной страницы приложения
    path('', views.home, name='home'),

    # API endpoints
    path('', include(router.urls)),
]