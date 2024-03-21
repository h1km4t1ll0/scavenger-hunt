from django.contrib import admin
from .forms import *


@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = [
        'telegram_id',
        'first_name',
        'second_name',
        'team'
    ]

    form = BotUserForm


@admin.register(BotUserState)
class BotUserStateAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'state'
    ]

    form = BotUserStateForm


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'unique_team_id',
        'members'
    ]

    def members(self, team: Team) -> str:
        return ''.join(f'{member.first_name} {member.second_name}' for member in team.botuser_set.all())

    form = TeamForm
