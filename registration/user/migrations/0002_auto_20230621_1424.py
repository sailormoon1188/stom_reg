# Generated by Django 2.2.19 on 2023-06-21 06:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(null=True, verbose_name='дата рождения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='comment',
            field=models.CharField(blank=True, max_length=255, verbose_name='комментарий'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="введите номер'телефона в формате: '+7xxxxxxxxxx'", regex='^\\+7\\d{9,14}$')], verbose_name='телефон'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('patient', 'Пациент'), ('admin', 'Администратор')], default='patient', help_text='Администратор или Аутентифицированный пользователь.По умолчанию `user`.', max_length=33, verbose_name='пользовательская роль'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255, unique=True, verbose_name='Имя пользователя'),
        ),
    ]