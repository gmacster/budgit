"""Contains views for various register-related models."""

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from budgit.register.models import (Account,
                                    Category,
                                    Payee,
                                    Transaction)
from budgit.register.serializers import (UserSerializer,
                                         GroupSerializer,
                                         AccountSerializer,
                                         CategorySerializer,
                                         PayeeSerializer,
                                         TransactionSerializer)

class UserViewSet(viewsets.ModelViewSet):
    """View for the User model."""
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """View for the User model."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class AccountViewSet(viewsets.ModelViewSet):
    """View for the User model."""
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """View for the Category model."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PayeeViewSet(viewsets.ModelViewSet):
    """View for the Payee model."""
    queryset = Payee.objects.all()
    serializer_class = PayeeSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    """View for the Transaction model."""
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
