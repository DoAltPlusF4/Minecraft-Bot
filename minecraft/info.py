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
            title="Minecraft Snapshots",
            colour=discord.Colour.green(),
            description="""
            __Minecraft Java:__
**Snapshot 20w22a**
https://www.minecraft.net/en-us/article/minecraft-snapshot-20w22a
• Piglins now sometimes dance in celebration of a completed hunt
• Villager workstation logic changes
• Bells can be hung from the underside of more blocks
• Added shader support for accessing depth buffer
• Experimental changes to graphics rendering
• Bug fixes

**Beta 1.16.0.64**
https://feedback.minecraft.net/hc/en-us/articles/360043752812
• New Nether biomes, blocks and structures no longer generate in worlds with a fixed version defined
• Fixed an issue that could cause tile entities in a chunk to lose their data when the chunk is loaded
• Cured zombie villagers can breed again
• Mobs that are path finding will be able to get to the end of their path
• Textures now load correctly when descending from high altitude 
• Add-on and scripting fixes
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
