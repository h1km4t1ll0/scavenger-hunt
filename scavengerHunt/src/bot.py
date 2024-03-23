import telebot

from scavengerHunt import settings
from scavengerHunt.models import BotUser, BotUserState, Task
from scavengerHunt.src.database import get_state
from scavengerHunt.src.handlers.test_logic import start_command, tasks_command, test_callback, test_solve

bot = telebot.TeleBot(settings.BOT_TOKEN)


def register_handlers(_bot: telebot.TeleBot):
    print("Registering handlers...")
    _bot.register_message_handler(start_command, commands=['start'],
                                  pass_bot=True)
    _bot.register_message_handler(tasks_command, commands=['tasks'],
                                  pass_bot=True)
    # check type of the task that is the first argument in call.data="TaskType TaskId"
    _bot.register_callback_query_handler(test_callback,
                                         func=lambda call: int(call.data.split()[0]) == Task.Type.SIMPLE, pass_bot=True)
    _bot.register_message_handler(test_solve,
                                  content_types=['text'],
                                  func=lambda message: get_state(
                                     BotUser.objects.get(telegram_id=message.from_user.id)) == BotUserState.State.SOLVING,
                                  pass_bot=True
                                  )


def pohuy():
    register_handlers(bot)
    bot.polling(none_stop=True, interval=5)
