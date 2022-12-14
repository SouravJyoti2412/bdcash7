# Generated by Django 4.1 on 2022-08-28 11:59

import Website_Setting.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website_Setting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='website_logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(help_text='our recommended size 20 KB MAX', upload_to='logo/', validators=[Website_Setting.models.validate_images], verbose_name='Website Logo')),
            ],
            options={
                'verbose_name': 'Website logo',
                'verbose_name_plural': 'Website Logo',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='homepage_animated_line',
            options={'managed': True, 'verbose_name': 'Animated Line', 'verbose_name_plural': 'Animated Line'},
        ),
        migrations.AlterModelTable(
            name='homepage_animated_line',
            table='',
        ),
    ]
