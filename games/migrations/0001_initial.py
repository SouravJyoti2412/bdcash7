# Generated by Django 4.1 on 2022-08-28 13:16

from django.db import migrations, models
import games.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='game1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fontImage', models.ImageField(help_text=' our recommended size  250 KB MAX', upload_to='games_image', validators=[games.models.validate_image], verbose_name='Game Image For Home page')),
                ('game_name', models.CharField(help_text='please enter Game name', max_length=30)),
                ('Image', models.ImageField(help_text='Please use our recommended dimensions: 887 X 885px, 200 KB MAX', upload_to='games_image', validators=[games.models.validate_images], verbose_name='Game Image')),
                ('rate', models.IntegerField(help_text='please enter how percent get customer', verbose_name='Winning Rate')),
            ],
        ),
        migrations.CreateModel(
            name='game2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fontImage', models.ImageField(help_text=' our recommended size  250 KB MAX', upload_to='games_image', validators=[games.models.validate_image], verbose_name='Game Image For Home page')),
                ('game_name', models.CharField(help_text='please enter Game name', max_length=30)),
                ('Image', models.ImageField(help_text='Please use our recommended dimensions: 887 X 885px, 200 KB MAX', upload_to='games_image', validators=[games.models.validate_images], verbose_name='Game Image')),
                ('rate', models.IntegerField(help_text='please enter how percent get customer', verbose_name='Winning Rate')),
            ],
        ),
        migrations.CreateModel(
            name='game3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fontImage', models.ImageField(help_text=' our recommended size  250 KB MAX', upload_to='games_image', validators=[games.models.validate_image], verbose_name='Game Image For Home page')),
                ('game_name', models.CharField(help_text='please enter Game name', max_length=30)),
                ('Image', models.ImageField(help_text='Please use our recommended dimensions: 887 X 885px, 200 KB MAX', upload_to='games_image', validators=[games.models.validate_images], verbose_name='Game Image')),
                ('rate', models.IntegerField(help_text='please enter how percent get customer', verbose_name='Winning Rate')),
            ],
        ),
        migrations.CreateModel(
            name='game4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fontImage', models.ImageField(help_text=' our recommended size  250 KB MAX', upload_to='games_image', validators=[games.models.validate_image], verbose_name='Game Image For Home page')),
                ('game_name', models.CharField(help_text='please enter Game name', max_length=30)),
                ('Image', models.ImageField(help_text='Please use our recommended dimensions: 887 X 885px, 200 KB MAX', upload_to='games_image', validators=[games.models.validate_images], verbose_name='Game Image')),
                ('rate', models.IntegerField(help_text='please enter how percent get customer', verbose_name='Winning Rate')),
            ],
        ),
        migrations.CreateModel(
            name='game5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fontImage', models.ImageField(help_text=' our recommended size  250 KB MAX', upload_to='games_image', validators=[games.models.validate_image], verbose_name='Game Image For Home page')),
                ('game_name', models.CharField(help_text='please enter Game name', max_length=30)),
                ('Image', models.ImageField(help_text='Please use our recommended dimensions: 887 X 885px, 200 KB MAX', upload_to='games_image', validators=[games.models.validate_images], verbose_name='Game Image')),
                ('rate', models.IntegerField(help_text='please enter how percent get customer', verbose_name='Winning Rate')),
            ],
        ),
        migrations.CreateModel(
            name='game6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fontImage', models.ImageField(help_text=' our recommended size  250 KB MAX', upload_to='games_image', validators=[games.models.validate_image], verbose_name='Game Image For Home page')),
                ('game_name', models.CharField(help_text='please enter Game name', max_length=30)),
                ('Image', models.ImageField(help_text='Please use our recommended dimensions: 887 X 885px, 200 KB MAX', upload_to='games_image', validators=[games.models.validate_images], verbose_name='Game Image')),
                ('rate', models.IntegerField(help_text='please enter how percent get customer', verbose_name='Winning Rate')),
            ],
        ),
    ]