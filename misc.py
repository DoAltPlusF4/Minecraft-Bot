import discord
from discord.ext import commands

import constants as c

class Misc(commands.Cog, name="Miscellaneous"):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
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
        print(ctx.message.content)
        print(ctx.message.author)
        print(ctx.message.guild)
        print('--------------------------------')
        await ctx.channel.trigger_typing()
        if ctx.guild.id == c.SERVER_ID:
            embed = discord.Embed(
                title='You are already in this server',
                description=
                f'However, you can still invite your friends with this link: {c.SERVER_INVITE}',
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
        print(ctx.message.content)
        print(ctx.message.author)
        print(ctx.message.guild)
        print('--------------------------------')
        await ctx.channel.trigger_typing()
        embed = discord.Embed(
            title='--> Vote for Minecraft Bot <--',
            colour=discord.Colour.green(),
            url='https://discordbots.org/bot/616308233950199828/vote'
        )
        embed.set_image(url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def senddiamonds(self, ctx, member: discord.User):
       print(ctx.message.content)
       print(ctx.message.author)
       print(ctx.message.guild)
       print('--------------------------------')
       await member.send('''Have some diamonds!!!!!!! ** Sent by {0} **
	<:diamond:616316009288040470> <:diamond:616316009288040470> <:diamond:616316009288040470> <:diamond:616316009288040470> <:diamond:616316009288040470> '''.format(ctx.message.author))
       await ctx.send('Sent!')
        
def setup(bot):
    bot.add_cog(Misc(bot))
