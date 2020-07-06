import discord
from discord.ext import commands

from . import constants as c
from . import misc

import os


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.remove_command("help")

        misc.setup(self)

    async def on_ready(self):
        """Set status and print client info."""
        self.support = self.get_guild(c.SERVER_ID)
        print("Logged on")
        print(self.user.name)
        await self.change_presence(
            status=discord.Status.online,
            activity=discord.Activity(
                name=f"Half-Life 3",
                type=discord.ActivityType.watching
            )
        )

    async def on_message(self, message):
        """Ignore bots."""
        if message.author.bot:
            return

        # Process Commands
        await self.process_commands(message)
