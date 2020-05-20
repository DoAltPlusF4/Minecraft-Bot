import discord
from discord.ext import commands


class NonPrefix(commands.Cog, name="Non-Prefix"):
    """Contains prefixless commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        """Check for any non-prefix commands."""
        if message.content.lower().startswith(
            "creeper"
        ):
            await message.channel.send("aw man")

        elif message.content.lower().startswith(
            "so we back in the mine"
        ):
            await message.channel.send(
                "got our pickaxe swinging from side to side, side, side to side")

        elif message.content.lower().startswith(
            "this task a gruelling one"
        ):
            await message.channel.send(
                "hope to find some diamonds to night, night, night diamonds tonight"
            )

        elif message.content.lower().startswith(
            "heads up"
        ):
            await message.channel.send("hear a sound, turn around and look up")

        elif message.content.lower().startswith(
            "pacer"
        ):
            await message.channel.send("yes")

        elif message.content.lower().startswith(
            "i could never forget those eyes"
        ):
            await message.channel.send("COS BABY TONIGHT")

        elif message.content.lower().startswith(
                "the creepers tryna steal all our stuff again"
        ):
            await message.channel.send("stuff again, 'gain, 'gain")


def setup(bot):
    bot.add_cog(NonPrefix(bot))
