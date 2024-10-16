'''from django.urls import path, include
from rest_framework.routers import DefaultRouter


    router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'users', UserProfileViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]






 
'''
# Initialize the DefaultRouter for handling API routing automatically

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, LibraryUserViewSet, TransactionViewSet, CustomUserViewSet

router = DefaultRouter()
router.register(r'customuser', CustomUserViewSet)
router.register(r'books', BookViewSet)
router.register(r'users', LibraryUserViewSet)
router.register(r'transactions', TransactionViewSet, basename='transaction')

# Define  custom transaction endpoints
transaction_list = TransactionViewSet.as_view({
    'post': 'checkout',  # Checkout book
})

transaction_return = TransactionViewSet.as_view({
    'post': 'return_book',  # Return book
})

urlpatterns = [
    path('api/', include(router.urls)),  # Ensure the API prefix is here
    path('api/transactions/checkout/<int:pk>/', transaction_list, name='transaction-checkout'),
    path('api/transactions/return/<int:pk>/', transaction_return, name='transaction-return'),
]
