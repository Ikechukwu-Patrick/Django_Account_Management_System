from decimal import Decimal

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Account, Transaction
from .serializer import AccountCreateSerializer


# Create your views here.

class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountCreateSerializer


# class ListAccount(ListCreateAPIView):
#     queryset = Account.objects.all()
#     serializer_class = AccountCreateSerializer

    # def get_queryset(self):
    #     return Account.objects.all()
    #
    # def get_serializer_class(self):
    #     return AccountCreateSerializer
    #
    #
    # def get(self, request):
    #     account = Account.objects.all()
    #     serializer = AccountSerializer(account, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    # def post(self, request):
    #     serializer = AccountCreateSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


# class AccountDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Account.objects.all()
#     serializer_class = AccountCreateSerializer

    # def get(self, request, pk):
    #     account = get_object_or_404(Account, pk=pk)
    #     serializer = AccountCreateSerializer(account)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    # def put(self, request, pk):
    #     serializer = AccountCreateSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    # def delete(self, request, pk):
    #     account = get_object_or_404(Account, pk=pk)
    #     account.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def list_account(request):
#     if request.method == 'GET':
#         account = Account.objects.all()
#         serializer = AccountSerializer(account, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = AccountCreateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(["GET", "PUT", "PATCH", "DELETE"])
# def account_detail(request, pk):
#     account = get_object_or_404(Account, pk=pk)
#     if request.method == 'GET':
#         serializer = AccountCreateSerializer(account)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == "PUT":
#         serializer = AccountCreateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PATCH':
#         serializer = AccountCreateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
# #     elif request.method == "DELETE":
#        account.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == "PATCH":
#         serializer = AccountCreateSerializer(account, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def deposit(request):
    account_number = request.data['account_number']
    amount = request.data['amount']
    account = get_object_or_404(Account, pk=account_number)
    if account.balance:
        account.balance += Decimal(amount)
        account.save()
        Transaction.objects.create(
            account=account,
            amount=amount,
            transaction_type="CRE"
        )
        return Response(data={"message": "Insufficient fund"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(data={"message": "Transaction successful"}, status=status.HTTP_200_OK)


@api_view(['POST'])
def withdraw(request):
    account_number = request.data['account_number']
    amount = request.data['amount']
    pin = request.data['pin']
    account = get_object_or_404(Account, pk=account_number)
    if account.pin == pin:
        if account.balance > amount:
            account.balance -= Decimal(amount)
            account.save()
            Transaction.objects.create(
                account=account,
                amount=amount,
                transaction_type="DEB"
            )
        else:
            return Response(data={"message": "Insufficient fund"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(data={"message": "Invalid pin"}, status=status.HTTP_400_BAD_REQUEST)

    return Response(data={"message": "Transaction successful"}, status=status.HTTP_200_OK)
