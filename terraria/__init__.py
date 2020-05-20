from . import (bot, constants, misc)
import os

submodules = [bot, constants, misc]

if __name__ == "__main__":
    terraria_bot = bot.Bot(
        command_prefix='t!',
        description="Something here!"
    )
    TOKEN = os.environ.get("terraria_token")
    bot.run(TOKEN, bot=True, reconnect=True)
