import asyncio
import os

import minecraft
import terraria

if __name__ == "__main__":
    mc_bot = minecraft.bot.Bot(
        command_prefix="m!",
        description="Now with added bullshit!"
    )
    terraria_bot = terraria.bot.Bot(
        command_prefix='t!',
        description="Something here!"
    )

    MC_TOKEN = os.environ.get("mc_token")
    TERRARIA_TOKEN = os.environ.get("terraria_token")

    loop = asyncio.get_event_loop()
    mc_task = loop.create_task(mc_bot.start(MC_TOKEN))
    terraria_task = loop.create_task(terraria_bot.start(TERRARIA_TOKEN))
    gathered = asyncio.gather(mc_task, terraria_task, loop=loop)
    loop.run_until_complete(gathered)
