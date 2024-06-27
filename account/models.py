from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.conf import settings
from .utils import generate_account_number
from .validators import validate_pin


# Create your models here.

class Account(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    account_number = models.CharField(max_length=10,
                                      default=generate_account_number, unique=True, primary_key=True)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    pin = models.CharField(max_length=4, validators=[validate_pin])
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    ACCOUNT_TYPES = [
        ('SAV', 'SAVING'),
        ('CUR', 'CURRENT'),
        ('DOM', 'DOMICILIARY'),

    ]
    account_type = models.CharField(max_length=3, choices=ACCOUNT_TYPES, default='s')

    def __str__(self):
        return f"{self.first_name} {self.second_name} {self.account_type}{self.account_number}"


class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('DEB', 'DEBIT'),
        ('CRE', 'CREDIT'),
        ('TRA', 'TRANSFER'),
    ]
    TRANSACTION_STATUS = [
        ('P', 'PENDING'),
        ('S', 'SUCCESSFUL'),
        ('F', 'FAILED'),
        ('R', 'REVERSED'),
    ]
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=3,
                                        choices=TRANSACTION_TYPES,
                                        default='CRE')
    transaction_time = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    transaction_status = models.CharField(max_length=1, choices=TRANSACTION_STATUS, default='S')

    def __str__(self):
        return f"{self.account} {self.amount} {self.transaction_status}"
