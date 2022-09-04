# Generated by Django 4.1 on 2022-08-30 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('all_payments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposite_amount', models.CharField(max_length=50, verbose_name='total deposite amount')),
                ('widthdrawl_amount', models.CharField(max_length=50, verbose_name='total withdrawl amount')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Deposit and withdrawl',
                'verbose_name_plural': 'Deposit and withdrawl',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
