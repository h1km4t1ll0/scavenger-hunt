import telebot

from scavengerHunt.models import Task, BotUserState, BotUser, Team
from scavengerHunt.src.keyboards import InlineKeyboard
from scavengerHunt.src.database import change_user_state


def start_command(message: telebot.types.Message, bot: telebot.TeleBot) -> None:
    bot.send_message(
        message.chat.id,
        "Welcome to the scavengerHunt bot!"
    )

    Team.objects.all().delete()
    BotUserState.objects.all().delete()
    BotUser.objects.all().delete()
    Task.objects.all().delete()

    team = Team(unique_team_id=1, name="a")
    team.save()
    bot_user = BotUser(telegram_id=message.from_user.id, team=team, first_name="DOLBOEB")
    bot_user.save()
    new_state = BotUserState(user=bot_user)
    new_state.save()
    task = Task(name="test", description="Correct answer is 13", answer="13")
    task.save()


def tasks_command(message: telebot.types.Message, bot: telebot.TeleBot) -> None:
    buttons = [(task.name, f'{task.type} {task.id}') for task in Task.objects.all()]  # BROKEN
    # (TypeOfTask, task type and task id)

    bot.send_message(
        message.chat.id,
        "Here is the list of tasks:",
        reply_markup=InlineKeyboard(buttons)
    )


def test_callback(call: telebot.types.CallbackQuery, bot: telebot.TeleBot) -> None:
    print("IN CALLBACK")
    # changing the state of a user and the task he is solving
    print(BotUser.objects.get(telegram_id=call.from_user.id))
    change_user_state(BotUser.objects.get(telegram_id=call.from_user.id),
                      BotUserState.State.SOLVING,
                      Task.objects.get(id=int(call.data.split()[1])))

    task_description = Task.objects.get(id=int(call.data.split()[1])).description  # call.data's second word is taskId

    bot.send_message(
        call.message.chat.id,
        task_description
    )


def test_solve(message: telebot.types.Message, bot: telebot.TeleBot) -> None:
    actual = message.text
    expected = BotUser.objects.get(telegram_id=message.from_user.id).botuserstate.task.answer

    if actual == expected:
        print("Correct answer")
        bot.send_message(
            message.chat.id,
            "Correct"
        )

        change_user_state(BotUser.objects.get(telegram_id=message.from_user.id), BotUserState.State.CHOOSING,
                          None)

        # TODO increase score
        # TODO add solved task to team
    else:
        print("Incorrect answer")
        bot.send_message(
            message.chat.id,
            "not correct"
        )
