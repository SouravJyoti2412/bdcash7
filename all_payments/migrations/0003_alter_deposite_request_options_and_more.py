# Generated by Django 4.1 on 2022-08-30 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('all_payments', '0002_transaction'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deposite_request',
            options={'managed': True, 'verbose_name': 'Deposite Request', 'verbose_name_plural': 'Deposite Request'},
        ),
        migrations.AlterModelTable(
            name='deposite_request',
            table='',
        ),
    ]