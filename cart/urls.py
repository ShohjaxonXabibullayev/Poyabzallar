from django.urls import path
from .views import CartCreate, AddToCart, CartItemUpdate

urlpatterns = [
    path('get-create/', CartCreate.as_view()),
    path('add-to-cart/', AddToCart.as_view()),
    path('cartitem-update/<int:pk>/', CartItemUpdate.as_view())
]