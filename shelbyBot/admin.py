from django.contrib import admin

from .forms import UserDAOForm, BlacklistDAOForm, OrderDaoForm
from .models import UserDAO, BlacklistDAO, OrderDao


@admin.register(UserDAO)
class UserDAOAdmin(admin.ModelAdmin):
    list_display = [
        'steamid',
        'default_step_key',
        'default_ref_key',
    ]

    form = UserDAOForm


@admin.register(BlacklistDAO)
class BlacklistDAOAdmin(admin.ModelAdmin):
    list_display = [
        'steamid',
    ]

    form = BlacklistDAOForm


@admin.register(OrderDao)
class OrderDaoAdmin(admin.ModelAdmin):
    list_display = [
        'bpid',
        'name',
        'max_key',
        'max_ref',
        'step_key',
        'step_ref',
        'is_active',
    ]

    form = OrderDaoForm
