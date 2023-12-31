# Generated by Django 2.2.16 on 2023-07-13 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EntryTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
                ('working_day', models.BooleanField(default=True, verbose_name='все дни по умолчанию отмеченыкак рабочие')),
                ('even_odd', models.CharField(choices=[('even_day', 'четный день'), ('odd_day', 'нечетный день')], help_text='Четный или нечетный рабочий день', max_length=33, verbose_name='четный или нечетный день')),
            ],
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procedure', models.CharField(max_length=150, verbose_name='название процедуры')),
                ('duration', models.DurationField(help_text='укажите времяпроцедуры в минутах', verbose_name='продолжительность процедуры в мин.')),
            ],
            options={
                'verbose_name': 'Процедура',
                'verbose_name_plural': 'Процедуры',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('enrty_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='date_time', to='entry.EntryTime')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to=settings.AUTH_USER_MODEL, verbose_name='Пациент')),
                ('procedure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='procedures', to='entry.Procedure')),
            ],
            options={
                'verbose_name': 'Запись на прием',
                'verbose_name_plural': 'Записи на прием',
            },
        ),
        migrations.AddConstraint(
            model_name='entry',
            constraint=models.UniqueConstraint(fields=('patient', 'enrty_time'), name='unique_patient_time'),
        ),
    ]
