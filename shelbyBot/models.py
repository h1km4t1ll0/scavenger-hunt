from django.db import models


class UserDAO(models.Model):
    steamid = models.TextField(
        verbose_name='Steam ID',
        null=False,
        blank=False
    )
    default_step_key = models.IntegerField(
        verbose_name='Ключи',
        null=False,
        blank=False,
        default=0
    )
    default_ref_key = models.IntegerField(
        verbose_name='Рефы',
        null=False,
        blank=False,
        default=0
    )
    objects = models.Manager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return '#' + str(self.steamid)


class BlacklistDAO(models.Model):
    steamid = models.TextField(
        verbose_name='Steam ID',
        null=False,
        blank=False
    )
    objects = models.Manager()

    class Meta:
        verbose_name = 'Забаненный аккаунт'
        verbose_name_plural = 'Забаненные аккаунты'

    def __str__(self):
        return '#' + str(self.steamid)


class OrderDao(models.Model):
    def __str__(self):
        return '#' + str(self.bpid)

    objects = models.Manager()
    bpid = models.TextField(
        verbose_name='Backpack ID',
        null=False,
        blank=False
    )
    name = models.TextField(
        verbose_name='Имя предмета',
        null=False,
        blank=False
    )
    max_key = models.IntegerField(
        verbose_name='Максимальное количество ключей',
        null=False,
        blank=False,
        default=0
    )
    max_ref = models.IntegerField(
        verbose_name='Максимальное количество рефов',
        null=False,
        blank=False,
        default=0
    )
    step_key = models.IntegerField(
        verbose_name='Шаг ключа',
        null=False,
        blank=False,
        default=0
    )
    step_ref = models.IntegerField(
        verbose_name='Шаг рефа',
        null=False,
        blank=False,
        default=0
    )
    is_active = models.BooleanField(
        verbose_name='Активно',
        null=False,
        blank=False,
        default=False
    )

    class Meta:
        verbose_name = 'Ордер'
        verbose_name_plural = 'Ордеры'
