
from rest_framework.routers import DefaultRouter

from django.urls import path,include
from .views import BookList
from .views import BookViewSet




router = DefaultRouter()
router.register(r'books', BookViewSet ,basename='book' )


urlpatterns = [
   
    path('book/',BookList.as_view(),name = 'book_list'),
    path('',include(router.urls)),
]



