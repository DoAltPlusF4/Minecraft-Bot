import discord
from discord.ext import commands

import constants as c


class Misc(commands.Cog, name="Miscellaneous"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Check the ping of the bot."""
        print(ctx.message.content)
        print(ctx.message.author)
        print(ctx.message.guild)
        print('--------------------------------')
        embed = discord.Embed(
            title='Bot Latency',
            description=f'**{int(self.bot.latency * 100)}**ms',
            colour=discord.Colour.green())
        return await ctx.send(embed=embed)

    @commands.command()
    async def server(self, ctx):
        """Get the invite for the support server."""
        print(ctx.message.content)
        print(ctx.message.author)
        print(ctx.message.guild)
        print('--------------------------------')
        await ctx.channel.trigger_typing()
        if ctx.guild.id == c.SERVER_ID:
            embed = discord.Embed(
                title='You are already in this server',
                description=f'However, you can still invite your friends with this link: {c.SERVER_INVITE}',
                colour=discord.Colour.green()
            )
        else:
            embed = discord.Embed(
                title='--> Minecraft Bot Official Server <--',
                colour=discord.Colour.green(),
                url=c.SERVER_INVITE
            )
        embed.set_image(url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def vote(self, ctx):
        """Get the link to vote for the bot."""
        print(ctx.message.content)
        print(ctx.message.author)
        print(ctx.message.guild)
        print('--------------------------------')
        await ctx.channel.trigger_typing()
        embed = discord.Embed(
            title="--> Vote for Minecraft Bot <--",
            colour=discord.Colour.green(),
            url=f"https://top.gg/bot/{self.bot.user.id}/vote"
        )
        embed.set_image(url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def senddiamonds(self, ctx, member: discord.User):
        """Send diamonds to a user.

        Arguments:
            member {discord.User} -- The user to send diamonds to.
        """
        print(ctx.message.content)
        print(ctx.message.author)
        print(ctx.message.guild)
        print('--------------------------------')
        await member.send(f"""
        Have some diamonds!!!!!!! ** Sent by {ctx.message.author} **
	    <:diamond:616316009288040470> <:diamond:616316009288040470> <:diamond:616316009288040470> <:diamond:616316009288040470> <:diamond:616316009288040470> 
        """)
        await ctx.send("Sent!")

    @commands.command()
    async def feedback(self, ctx, *, feedback):
        """Sends user feedback to the owners."""

        for id in c.OWNERS:
            user = self.bot.get_user(id)
            await user.send(f"""
            **Feedback, sent by `{ctx.author}`:**
            {feedback}
            """)

        await ctx.send("Sent!")

    @commands.command()
    async def help(self, ctx):
        "Commands for Minecraft Bot"
        print(ctx.message.content)
        print(ctx.message.author)
        print(ctx.message.guild)
        embed = discord.Embed(
            title="Minecraft Bot Commands",
            description='''
            *Prefix = m!*
            __**Minecraft Info:**__
  bedrock      Get info about Minecraft Bedrock edition.
  blocks       Get the amount of blocks in Minecraft.
  java         Get info about Minecraft Java edition.
  snapshots    Get info about the current snapshots.
  wiki         Get the link to the Minecraft Wiki.
__**Miscellaneous:**__
  feedback     Sends user feedback to the owners.
  ping         Check the ping of the bot.
  senddiamonds Send diamonds to a user.
  server       Get the invite for the support server.
  vote         Get the link to vote for the bot.
__**Mob Info:**__
  cow          Send info about the Cow mob.
  enderdragon  Send info about the Enderdragon mob/boss.
  pig          Send info about the Pig mob.
  sheep        Send info about the Sheep mob.
  skeleton     Send info about the Skeleton mob.
  spider       Send info about the Spider mob.
  wither       Send info about the Wither mob/boss.
  zombie       Send info about the Zombie mob.
  zombiepigman Send info about the Zombie Pigman mob.

  Bot Created by matthew#8906 and ( ͡° ͜ʖ ͡°)#0001
''',
            colour=discord.Colour.green()
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Misc(bot))
