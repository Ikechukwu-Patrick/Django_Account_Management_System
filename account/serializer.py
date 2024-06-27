from rest_framework import serializers
from .models import Account, Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'transaction_type', 'transaction_time', 'transaction_status', 'description']


class AccountSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True)

    class Meta:
        model = Account
        fields = ['account_number', 'first_name', 'second_name', 'balance', 'account_type', 'transactions']
        #transactions = serializers.StringRelatedField()


class AccountCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['first_name', 'second_name', 'pin', 'account_type']
