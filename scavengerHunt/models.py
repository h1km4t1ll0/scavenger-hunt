from django.db import models
from django.utils.translation import gettext_lazy as _

from scavengerHunt.src.shared import gen_uuid


class Team(models.Model):
    name = models.TextField(
        verbose_name='Название команды',
        null=False,
        blank=False
    )

    unique_team_id = models.CharField(
        verbose_name='Идентификатор команды',
        unique=True,
        null=False,
        blank=False,
        max_length=40,
        default=gen_uuid()
    )

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'


class BotUser(models.Model):
    telegram_id = models.BigIntegerField(
        primary_key=True,
        verbose_name='ID в телеграм',
        null=False,
        blank=False,
    )

    first_name = models.TextField(
        verbose_name='Имя',
        null=True,
        blank=False,
    )

    second_name = models.TextField(
        verbose_name='Фамилия',
        null=True,
        blank=False,
    )

    team = models.ForeignKey(
        to=Team,
        on_delete=models.CASCADE,
        verbose_name='Команда'
    )

    objects = models.Manager()

    def __str__(self):
        return f'{self.first_name} {self.second_name}'

    class Meta:
        verbose_name = 'Пользователь бота'
        verbose_name_plural = 'Пользователи бота'


class BotUserState(models.Model):
    class State(models.IntegerChoices):
        REGISTER = 0, _("Регистрация")
        SOLVING = 1, _("Решает")

    state = models.IntegerField(
        choices=State,
        default=State.REGISTER,
    )

    user = models.OneToOneField(
        to=BotUser,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Состояние пользователя'
        verbose_name_plural = 'Состояния пользователей'
