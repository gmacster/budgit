"""Contains views for various register-related models."""

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from budgit.register import models, serializers

class UserViewSet(viewsets.ModelViewSet):
    """View for the User model."""
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """View for the User model."""
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer

class AccountViewSet(viewsets.ModelViewSet):
    """View for the User model."""
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountSerializer

class MasterCategoryViewSet(viewsets.ModelViewSet):
    """View for the MasterCategory model."""
    queryset = models.MasterCategory.objects.all()
    serializer_class = serializers.MasterCategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """View for the Category model."""
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

class PayeeViewSet(viewsets.ModelViewSet):
    """View for the Payee model."""
    queryset = models.Payee.objects.all()
    serializer_class = serializers.PayeeSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    """View for the Transaction model."""
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer
