from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('<slug:category_slug>/', views.store, name='products_by_category'),
    path('subcategory/<slug:subcategory_slug>/', views.subcategory_view, name='subcategory_detail'),
    path('<slug:subcategory_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('<slug:category_slug>/', views.store, name='store_by_category'),
    path('<slug:category_slug>/<slug:subcategory_slug>/', views.store, name='store_by_subcategory'),
    path('search/', views.search, name='search'),
    path('submit_review/<int:product_id>/',views.submit_review,name="submit_review"),
    path('store/submit_review/<int:product_id>/', views.submit_review, name='submit_review'),
]
