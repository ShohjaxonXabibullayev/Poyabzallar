from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from Auth.user_perm import IsUser
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination


class PoyabzalListCreate(APIView):
    permission_classes = [permissions.IsAuthenticated, IsUser]
    def get(self, request):
        poyabzal = Poyabzallar.objects.all()
        category = request.GET.get('category')
        price = request.GET.get('price')
        if category:
            poyabzal = poyabzal.filter(Category__name=category)
        if price:
            poyabzal = poyabzal.filter(price=price)
        search = request.GET.get('search')
        if search:
            poyabzal = poyabzal.filter(Q(name__icontains=search) | Q(type__icontains=search))
        ordering = request.GET.get('ordering')
        if ordering:
            poyabzal = poyabzal.order_by(ordering)

        paginator = PageNumberPagination()
        paginator.page_size = 3
        paginated_queryset = paginator.paginate_queryset(poyabzal, request)

        serializer = PoyabzalSerializer(paginated_queryset, many=True)
        data = {
            'status': status.HTTP_200_OK,
            'results': serializer.data
        }
        return paginator.get_paginated_response(data)

    def post(self, request):
        serializer = PoyabzalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'status': status.HTTP_200_OK})
        return Response({'status': status.HTTP_400_BAD_REQUEST, 'error': serializer.errors})


class PoyabzalCRUD(APIView):
    permission_classes = [permissions.IsAuthenticated, IsUser]

    def get(self, request, pk):
        try:
            poyabzal = Poyabzallar.objects.get(id=pk)
        except Poyabzallar.DoesNotExist:
            return Response({'status': status.HTTP_404_NOT_FOUND, 'error': 'Poyabzal topilmadi'})
        serializer = PoyabzalSerializer(poyabzal)
        return Response({'data': serializer.data, 'status': status.HTTP_200_OK})

    def patch(self, request, pk):
        try:
            poyabzallar = Poyabzallar.objects.get(id=pk)
        except Poyabzallar.DoesNotExist:
            return Response({'status': status.HTTP_404_NOT_FOUND, 'error': 'Poyabzal topilmadi'})
        serializer = PoyabzalSerializer(instance=poyabzallar, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'message': 'Poyabzal yangilandi', 'data': serializer.data, 'status': status.HTTP_200_OK})
        return Response({'status': status.HTTP_400_BAD_REQUEST, 'error': serializer.errors})

    def put(self, request, pk):
        try:
            poyabzal = Poyabzallar.objects.get(id=pk)
        except Poyabzallar.DoesNotExist:
            return Response({'status': status.HTTP_404_NOT_FOUND, 'error': 'Poyabzal topilmadi'})
        serializer = PoyabzalSerializer(instance=poyabzal, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'message': 'Poyabzal yangilandi', 'data': serializer.data, 'status': status.HTTP_200_OK})
        return Response({'status': status.HTTP_400_BAD_REQUEST, 'error': serializer.errors})

    def delete(self, request, pk):
        try:
            poyabzal = Poyabzallar.objects.get(id=pk)
            poyabzal.delete()
        except Poyabzallar.DoesNotExist:
            return Response({'status': status.HTTP_404_NOT_FOUND, 'error': 'id mavjud emas'})
        return Response({'message': 'O‘chirildi', 'status': status.HTTP_200_OK})


class CommentApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if request.user.is_staff:
            comments = Comments.objects.all()
        else:
            comments = Comments.objects.filter(user=request.user)

        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        try:
            comment = Comments.objects.get(pk=pk)
        except Comments.DoesNotExist:
            return Response({'error': 'Comment topilmadi'}, status=status.HTTP_404_NOT_FOUND)

        if request.user == comment.user or request.user.is_staff:
            comment.delete()
            return Response({'msg': "Comment o'chirildi"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': "Siz bu komentni o'chira olmaysiz"}, status=status.HTTP_403_FORBIDDEN)
