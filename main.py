import asyncio
import os

import minecraft

if __name__ == "__main__":
    mc_bot = minecraft.bot.Bot(
        command_prefix="m!",
        description="Now with added bullshit!"
    )

    MC_TOKEN = os.environ.get("mc_token")

    loop = asyncio.get_event_loop()
    mc_task = loop.create_task(mc_bot.start(MC_TOKEN))
    gathered = asyncio.gather(mc_task, loop=loop)
    loop.run_until_complete(gathered)
