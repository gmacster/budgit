"""Contains serializers for various register-related models."""

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from budgit.register.models import (Account,
                                    Category,
                                    Payee,
                                    Transaction)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the User model."""
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the Group model."""
    class Meta:
        model = Group
        fields = ('url', 'name')

class AccountSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the Account model."""
    class Meta:
        model = Account
        fields = '__all__'

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the Category model."""
    class Meta:
        model = Category
        fields = '__all__'

class PayeeSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the Payee model."""
    class Meta:
        model = Payee
        fields = '__all__'

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the Transaction model."""
    class Meta:
        model = Transaction
        fields = '__all__'
