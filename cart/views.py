from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from products.models import Poyabzallar
from .serializers import CartSerializer, CartItemSerializer
from .models import CartItem, Cart
from Auth.user_perm import IsUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class CartCreate(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)

class AddToCart(APIView):
    permission_classes = [IsUser, ]
    def post(self, request):
        product_id = request.data['product_id']
        amount = int(request.data['amount'])

        if not Poyabzallar.objects.filter(id=product_id).exists():
            data = {'error':'Siz mavjud bolmagan poyabzalni tanladingiz',
                    'status':status.HTTP_400_BAD_REQUEST}

            return Response(data)
        if amount <= 0 or amount > 100:
            data = {'error':'Siz xato malumot kiritdingiz',
                    'status':status.HTTP_400_BAD_REQUEST}
            return Response(data)

        cart, _ = Cart.objects.get_or_create(user=request.user)

        poyabzal = Poyabzallar.objects.get(id=product_id)

        if not CartItem.objects.filter(cart=cart, product=poyabzal).exists():
            poyabzal = CartItem.objects.create(
                cart=cart,
                product=poyabzal,
                amount=amount
            )
        else:
            poyabzal = CartItem.objects.get(cart=cart, product=poyabzal)
            poyabzal.amount += amount

        poyabzal.save()

        serializer = CartItemSerializer(poyabzal)
        data = {'data': serializer.data,
                'status': status.HTTP_201_CREATED}
        return Response(data)


class CartItemUpdate(APIView):
    permission_classes = [IsUser, ]
    def post(self, request, pk):
        count = request.data.get('count', None)
        mtd = request.data.get('mtd', None)

        product = CartItem.objects.get(cart__user=request.user, id=pk)
        if count:
            product.amount = int(count)
            product.save()

        elif mtd:
            if mtd == '+':
                product.amount += 1
            elif mtd == '-':
                if product.amount == 1:
                    product.delete()
                else:
                    product.amount -= 1
            product.save()


        else:
            return Response({'error':'Error', 'status':status.HTTP_400_BAD_REQUEST})

        serializer = CartItemSerializer(product)
        data = {
            'data':serializer.data,
            'status':status.HTTP_200_OK,
            'msg': "O'zgartitldi!"
        }
        return Response(data)


