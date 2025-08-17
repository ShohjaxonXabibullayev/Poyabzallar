from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CreateOrderAPIView.as_view(), name='order-create')
]