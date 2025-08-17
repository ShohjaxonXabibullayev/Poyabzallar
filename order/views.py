from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Order, OrderItem
from .serializers import OrderSerializer
from products.models import Poyabzallar
from cart.models import Cart, CartItem


class CreateOrderAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            cart = request.user.cart
        except Cart.DoesNotExist:
            return Response(
                {"xatolik": "Savatchangiz topilmadi"},
                status=status.HTTP_400_BAD_REQUEST
            )


        if not cart.items.exists():
            return Response(
                {"xatolik": "Savatchangiz bo‘sh"},
                status=status.HTTP_400_BAD_REQUEST
            )


        order = Order.objects.create(user=request.user)

        for cart_item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                amount=cart_item.amount
            )


        cart.items.all().delete()


        serializer = OrderSerializer(order)
        return Response(
            {
                "xabar": "Zakazingiz qabul qilindi ",
                "order": serializer.data
            },
            status=status.HTTP_201_CREATED
        )
