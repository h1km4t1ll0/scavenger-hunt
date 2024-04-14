from django import forms

from .models import UserDAO, BlacklistDAO, OrderDao


class UserDAOForm(forms.ModelForm):
    class Meta:
        model = UserDAO
        fields = (
            'steamid',
            'default_step_key',
            'default_ref_key',
        )


class BlacklistDAOForm(forms.ModelForm):
    class Meta:
        model = BlacklistDAO
        fields = (
            'steamid',
        )


class OrderDaoForm(forms.ModelForm):
    class Meta:
        model = OrderDao
        fields = (
            'name',
            'max_key',
            'max_ref',
            'step_key',
            'step_ref',
            'is_active',
        )
