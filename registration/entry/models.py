from django.db import models
from user.models import User


class Procedure(models.Model):
    procedure = models.CharField('название процедуры', max_length=150,
                                 blank=False)
    duration = models.DurationField('продолжительность процедуры в мин.',
                                    blank=False,
                                    help_text='укажите время'
                                    'процедуры в минутах')

    class Meta:
        verbose_name = "Процедура"
        verbose_name_plural = "Процедуры"

    def __str__(self):
        return self.procedure


class EntryTime(models.Model):
    DAYS = (
        ('even_day', 'четный день'),
        ('odd_day', 'нечетный день'),
    )
    date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    working_day = models.BooleanField('все дни по умолчанию отмечены'
                                      'как рабочие',
                                      default=True)
    even_odd = models.CharField(
        'четный или нечетный день',
        max_length=33,
        help_text='Четный или нечетный рабочий день',
        choices=DAYS,
    )

    def __str__(self):
        return f'{self.date}: {self.start_time} - {self.end_time} {self.even_odd}'


class Entry(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='entries',
        verbose_name='Пациент'
    )
    procedure = models.ForeignKey(
        Procedure,
        related_name='procedures',
        on_delete=models.CASCADE
    )
    enrty_time = models.ForeignKey(
        EntryTime,
        related_name='date_time',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Запись на прием'
        verbose_name_plural = 'Записи на прием'
        constraints = [
            models.UniqueConstraint(
                fields=['patient', 'enrty_time'], name='unique_patient_time'
            )
        ]

    def __str__(self):
        return (f'{self.patient} записан на {self.enrty_time} '
                f'на {self.procedure}')
