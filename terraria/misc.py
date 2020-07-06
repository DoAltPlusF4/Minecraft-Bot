import discord
from discord.ext import commands

from . import constants as c

class Misc(commands.Cog, name="Miscellaneous"):
    """Miscellaneous commands, includes Ping, Vote and the Support server."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(
            title='Bot Latency',
            description='**{0}**ms'.format(int(bot.latency * 100)),
            colour=discord.Colour.orange())
        return await ctx.send(embed=embed)
    
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            title='Half-Life Bot Help Page',
            description='''	
        Prefix = 'hl!'

        **Game related Commands:**
        hl!halflife - Info about the game Half-Life
        hl!oppforce - Info about the game Half-Life: Opposing Force
        hl!blueshift - Info about the game Half-Life: Blue Shift
        hl!decay - Info about the game Half-Life: Decay
        hl!halflifesource - Info about the game Half-Life: Source
        hl!halflifedmsource - Info about the game Half-Life Deathmatch: Source
        hl!halflife2 - Info about the game Half-Life 2
        hl!halflife2dm - Info about the game Half-Life 2: Deathmatch
        hl!halflife2ep1 - Info about the game Half-Life 2: Episode 1
        hl!halflife2ep2 - Info about the game Half-Life 2: Episode 2
        hl!halflife2lostcoast - Info about the game Half-Life 2: Lost Coast
        hl!blackmesa - Info about the game Black Mesa
        hl!other - Info about any other notable games

		**Other Commands**:
		hl!help - displays this message
        hl!ping - bot latency test

		Minecraft Bot Official Server: https://discord.gg/X6cxXck
		''',
            color=discord.Colour.orange())
        embed.set_footer(text='Bot made by matthew#8906')
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Misc(bot))
