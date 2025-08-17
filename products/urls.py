from django.urls import path
from .views import *

urlpatterns = [
    path('', PoyabzalListCreate.as_view(), name='ListCreate'),
    path('detail/<int:pk>/', PoyabzalCRUD.as_view(), name='detail'),
    path('comments/', CommentApiView.as_view(), name="comment-list-create"),
    path('comments/<int:pk>/', CommentDetailApiView.as_view(), name="comment-detail"),
]