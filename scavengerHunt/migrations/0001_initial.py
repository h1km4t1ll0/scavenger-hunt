# Generated by Django 5.0.3 on 2024-03-21 03:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotUser',
            fields=[
                ('telegram_id', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='ID в телеграм')),
                ('first_name', models.TextField(null=True, verbose_name='Имя')),
                ('second_name', models.TextField(null=True, verbose_name='Фамилия')),
            ],
            options={
                'verbose_name': 'Пользователь бота',
                'verbose_name_plural': 'Пользователи бота',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название команды')),
                ('unique_team_id', models.CharField(default='c9c46fc9-cf2f-4051-bd8b-d8d48e0bf099', max_length=40, unique=True, verbose_name='Идентификатор команды')),
            ],
            options={
                'verbose_name': 'Команда',
                'verbose_name_plural': 'Команды',
            },
        ),
        migrations.CreateModel(
            name='BotUserState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(choices=[(0, 'Регистрация'), (1, 'Решает')], default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='scavengerHunt.botuser')),
            ],
            options={
                'verbose_name': 'Состояние пользователя',
                'verbose_name_plural': 'Состояния пользователей',
            },
        ),
        migrations.AddField(
            model_name='botuser',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scavengerHunt.team', verbose_name='Команда'),
        ),
    ]
