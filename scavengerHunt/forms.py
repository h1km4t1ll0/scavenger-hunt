from django import forms
from .models import *


class BotUserForm(forms.ModelForm):
    class Meta:
        model = BotUser
        fields = (
            'telegram_id',
            'first_name',
            'second_name',
            'team'
        )

        widgets = {
            'first_name': forms.TextInput,
            'second_name': forms.TextInput,
        }


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = (
            'name',
            'unique_team_id'
        )

        widgets = {
            'name': forms.TextInput,
            'unique_team_id': forms.TextInput
        }


class BotUserStateForm(forms.ModelForm):
    class Meta:
        model = BotUserState
        fields = (
            'state',
            'user'
        )
