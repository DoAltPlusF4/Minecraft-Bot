import os

import discord
import heroku3
import redis
from discord.ext import commands

import constants as c
import info
import misc
import mobs
import non_prefix

bot.remove_command('help')

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        """Initialise client, make support server attribute."""
        super().__init__(*args, **kwargs)
        # self.remove_command("help")

    async def on_ready(self):
        """Set status and print client info."""
        self.support = self.get_guild(c.SERVER_ID)
        print('Logged on')
        print(self.user.name)
        await self.change_presence(
            status=discord.Status.dnd,
            activity=discord.Activity(
                name=f"Mining Diamonds with {len(self.guilds)} servers!",
                type=discord.ActivityType.playing
            )
        )

        # Cogs Setup
        non_prefix.setup(self)
        info.setup(self)
        mobs.setup(self)
        misc.setup(self)

    async def on_message(self, message):
        """Ignore bots."""
        if message.author.bot:
            return

        # Process Commands
        await self.process_commands(message)

    async def on_member_join(self, member):
        """Send welcome message."""
        if member.guild.id == c.SERVER_ID:
            channel = self.support.get_channel(c.WELCOME_CHANNEL)
            embed = discord.Embed(
                title=f"Welcome, **{member.nick if member.nick is not None else member.name}**!",
                description="""
                Welcome to the official **Minecraft Bot support server**.

                You can place your bot suggestions in the <#697360065463713834> channel,
                and can ask for support in the <#697394845140123660> channel.
                """,
                colour=discord.Colour.teal()
            )
            embed.set_thumbnail(url=self.support.icon_url)
            await channel.send(embed=embed)


if __name__ == "__main__":
    bot = Bot(command_prefix='m!',
              description="I'll get better help formatting soon, I swear!")
    TOKEN = os.environ.get("token")
    bot.run(TOKEN, bot=True, reconnect=True)
