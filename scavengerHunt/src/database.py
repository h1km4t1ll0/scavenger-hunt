from scavengerHunt.models import BotUser, BotUserState, Task


# to get state of the user
def get_state(bot_user: BotUser) -> BotUserState:
    return BotUserState.objects.get(user=bot_user).state


def change_user_state(bot_user: BotUser, state: int, task: Task):
    bot_user = bot_user.botuserstate.task
    bot_user.state = state
    bot_user.task = task
    bot_user.save()
