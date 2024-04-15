# Generated by Django 5.0.4 on 2024-04-14 13:29

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlacklistDAO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steamid', models.TextField(verbose_name='Steam ID')),
            ],
            options={
                'verbose_name': 'Забаненный аккаунт',
                'verbose_name_plural': 'Забаненные аккаунты',
            },
        ),
        migrations.CreateModel(
            name='OrderDao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bpid', models.TextField(verbose_name='Backpack ID')),
                ('name', models.TextField(verbose_name='Имя предмета')),
                ('max_key', models.IntegerField(default=0, verbose_name='Максимальное количество ключей')),
                ('max_ref', models.IntegerField(default=0, verbose_name='Максимальное количество рефов')),
                ('step_key', models.IntegerField(default=0, verbose_name='Шаг ключа')),
                ('step_ref', models.IntegerField(default=0, verbose_name='Шаг рефа')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активно')),
            ],
            options={
                'verbose_name': 'Ордер',
                'verbose_name_plural': 'Ордеры',
            },
        ),
        migrations.CreateModel(
            name='UserDAO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steamid', models.TextField(verbose_name='Steam ID')),
                ('default_step_key', models.IntegerField(default=0, verbose_name='Ключи')),
                ('default_ref_key', models.IntegerField(default=0, verbose_name='Рефы')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
