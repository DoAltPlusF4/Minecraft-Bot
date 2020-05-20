from . import (bot, constants, info, misc, mobs, non_prefix)
import os

submodules = [bot, constants, info, misc, mobs, non_prefix]

if __name__ == "__main__":
    mc_bot = bot.Bot(
        command_prefix='m!',
        description="I'll get better help formatting soon, I swear!"
    )
    TOKEN = os.environ.get("token")
    bot.run(TOKEN, bot=True, reconnect=True)
