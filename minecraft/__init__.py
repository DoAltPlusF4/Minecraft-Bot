from . import (bot, constants, info, misc, mobs, non_prefix)
import os

submodules = [bot, constants, info, misc, mobs, non_prefix]

if __name__ == "__main__":
    mc_bot = bot.Bot(
        command_prefix='m!',
        description="Now with added bullshit!"
    )
    TOKEN = os.environ.get("mc_token")
    bot.run(TOKEN, bot=True, reconnect=True)
