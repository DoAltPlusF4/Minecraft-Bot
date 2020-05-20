import asyncio
import os

import minecraft

if __name__ == "__main__":
    mc_bot = minecraft.bot.Bot(
        command_prefix="m!",
        description="I'll get better help formatting soon, I swear!"
    )
    MC_TOKEN = os.environ.get("mc_token")
    mc_bot.run(MC_TOKEN, bot=True, reconnect=True)
