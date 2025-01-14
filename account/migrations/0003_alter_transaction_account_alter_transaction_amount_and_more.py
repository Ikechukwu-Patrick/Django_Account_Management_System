# Generated by Django 5.0.6 on 2024-06-26 17:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_account_balance_alter_account_pin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='account.account'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_status',
            field=models.CharField(choices=[('P', 'PENDING'), ('S', 'SUCCESSFUL'), ('F', 'FAILED'), ('R', 'REVERSED')], default='S', max_length=1),
        ),
    ]
