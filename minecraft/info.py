import discord
from discord.ext import commands


class MinecraftInfo(commands.Cog, name="Minecraft Info"):
    """Contains commands about minecraft info."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def blocks(self, ctx):
        """Get the amount of blocks in Minecraft."""
        print(ctx.message.content)
        print(ctx.message.author)
        print(ctx.message.guild)
        print("--------------------------------")
        await ctx.channel.send("There are more than 150 blocks in minecraft!")

    @commands.command()
    async def snapshots(self, ctx):
        """Get info about the current snapshots."""
        print(ctx.message.content)
        print(ctx.message.author)
        print(ctx.message.guild)
        await ctx.channel.trigger_typing()
        embed = discord.Embed(
            title="Newest Minecraft Snapshots",
            colour=discord.Colour.green(),
            description="""
            __Minecraft Java:__
**1.16.1**
https://www.minecraft.net/en-us/article/minecraft-java-edition-1-16-1
• Realms stability fixes.

**Beta 1.16.20.50**
https://feedback.minecraft.net/hc/en-us/articles/360045006632
• Added Piglin Brute mob
• Updated Piglin geometry and entity files
• New Nether biomes, blocks and structures no longer generate in worlds with a fixed version
• Netherite items in lava no longer disappear when reloading world
• Fixed several issues with duplicating items that could occur when reloading a world while Piglin is admiring an item 
• Bug fixes
            """)
        await ctx.send(embed=embed)

    @commands.command()
    async def wiki(self, ctx):
        """Get the link to the Minecraft Wiki."""
        print(ctx.message.content)
        print(ctx.message.author)
        print(ctx.message.guild)
        print("--------------------------------")
        embed = discord.Embed(
            title="Minecraft Wiki",
            description="https://minecraft.gamepedia.com/Minecraft_Wiki",
            color=discord.Colour.blue())
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def bedrock(self, ctx):
        """Get info about Minecraft Bedrock edition."""
        print(ctx.message.content)
        print(ctx.message.author)
        print(ctx.message.guild)
        print("--------------------------------")
        await ctx.channel.trigger_typing()
        embed = discord.Embed(
            title="Bedrock is available on:",
            description="Phone and Tablet (Android, IOS, Fire OS, Windows Mobile), Windows 10, Nintendo Switch, Xbox One, PS4, Fire TV and Gear VR. Learn more about Bedrock  at https://minecraft.gamepedia.com/Bedrock_Edition",
            colour=discord.Colour.green())
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def java(self, ctx):
        """Get info about Minecraft Java edition."""
        print(ctx.message.content)
        print(ctx.message.author)
        print(ctx.message.guild)
        print("--------------------------------")
        await ctx.channel.trigger_typing()
        embed = discord.Embed(
            title="Java Edition is available on:",
            description="Linux, MacOS and Windows. Learn more about Java Edition  at https://minecraft.gamepedia.com/Java_Edition",
            colour=discord.Colour.green())
        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(MinecraftInfo(bot))
