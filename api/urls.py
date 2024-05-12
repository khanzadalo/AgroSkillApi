from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('product', views.ProductView)
router.register('user', views.UserView)
router.register('category', views.CategoryView)

urlpatterns = [
    path('', include(router.urls)),
    path('cart/', views.CartItemView.as_view(), name="cart"),
    path('cart/add/', views.CartItemAddView.as_view(), name="cart_add"),
    path('cart/delete/<int:pk>/', views.CartItemDelView.as_view(), name="cart_delete"),
    path('cart/add_one/<int:pk>/', views.CartItemAddOneView.as_view(), name="cart_add_one"),
    path('cart/reduce_one/<int:pk>/', views.CartItemReduceOneView.as_view(), name="cart_reduce_one"),

]
