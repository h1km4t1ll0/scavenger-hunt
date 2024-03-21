import django.http
import telebot

from scavengerHunt import settings
from scavengerHunt.src.bot import bot
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import scavengerHunt.settings


@csrf_exempt
def get_message(request: django.http.HttpRequest):
    if request.method == 'POST':
        json_string = request.body.decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return HttpResponse('!', 200)
    return HttpResponse('Method Not Allowed', 405)


if not settings.DEBUG:
    bot.set_webhook(url=f'https://{settings.DOMAIN}/{settings.BOT_TOKEN}')
