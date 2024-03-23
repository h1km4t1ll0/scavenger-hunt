from scavengerHunt.models import BotUser, BotUserState, Task


def change_user_state(bot_user: BotUser, new_state: int, task: Task):
    print(f'\nCHANGING STATE OF {bot_user.botuserstate.user} {bot_user.botuserstate.state} {bot_user.botuserstate.task}')
    bot_user_state = bot_user.botuserstate
    bot_user_state.state = new_state
    bot_user_state.task = task
    bot_user_state.save()
    print("STATE WAS CHANGED\n")
