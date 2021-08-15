from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('user_page/', views.userPage, name='user_page'),
    path('dashboard/', views.home, name='dashboard'),
    path('products/', views.products, name='products'),
    path('customer/<int:pk>/', views.customer, name='customer_details'),
    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<int:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<int:pk>/', views.deleteOrder, name="delete_order"),
]
