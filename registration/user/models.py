from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


from django.db import models


class User(AbstractUser):
    ROLES = (
        ('patient', 'Пациент'),
        ('admin', 'Администратор'),
    )
    DEFAULT_ROLE = ROLES[0][0]
    SEX = (
        ('man', 'мужской'),
        ('woman', 'женский'),
    )

    username = models.CharField(
        'Имя пользователя',
        unique=True, max_length=255
    )
    password = models.CharField('пароль', max_length=150)

    first_name = models.CharField('имя', max_length=150, blank=False)
    patronymic = models.CharField('отчество', max_length=150, blank=False)
    last_name = models.CharField('фамилия', max_length=150, blank=False)
    birth_date = models.DateField('дата рождения', null=True)
    sex = models.CharField(
        'пол',
        help_text='укажите пол пациента.',
        choices=SEX,
        max_length=10,
        blank=False
    )

    phone_regex = RegexValidator(
        regex=r'^\+7\d{9,14}$',
        message="введите номер'телефона в формате: '+7xxxxxxxxxx'"
        )
    phone_number = models.CharField(
        'телефон', validators=[phone_regex],
        max_length=15
        )
    email = models.EmailField(
        'почта',
        max_length=254,
        blank=False,
        unique=True
    )
    comment = models.CharField('комментарий', max_length=255, blank=True)
    role = models.CharField(
        'пользовательская роль',
        max_length=33,
        help_text='Администратор или Аутентифицированный пользователь.'
        'По умолчанию `user`.',
        choices=ROLES,
        default=DEFAULT_ROLE
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name', 'username', )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ('id', )

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_user(self):
        return self.role == 'user'
