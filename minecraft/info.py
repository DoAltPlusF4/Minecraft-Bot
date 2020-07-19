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
**Snapshot 20w29a**
https://www.minecraft.net/en-us/article/minecraft-snapshot-20w29a
• Tools are now sorted based on material in the creative inventory.
• New parameter for spawnpoint and setworldspawn: angle - setting the default facing angle of a respawning player.
• Customized world generation: worldgen/noise_settings  can now contain noise configurations.
• Fixed an issue that could cause bone meal to not create flowers.
• Fixes an issue that could cause birch trees to not generate correctly in the Birch Forest and Birch Forest Hills biomes.
• Bugs fixes.

            __Minecraft Bedrock:__
**Beta 1.16.20.53**
https://feedback.minecraft.net/hc/en-us/articles/360045908892
• Improved highlighting and selecting recipes when using a controller
• Loom blocks will no longer cause an out of memory crash when using high resolution resource packs 
• Opening old worlds will no longer cause chunks to become 100% air
• Piglins and Piglin Brutes can now spawn with enchanted weapons
• Bug fixes
            """)
        embed.set_footer(text="Remember to vote on top.gg! m!vote")
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
        embed.set_footer(text="Remember to vote on top.gg! m!vote")
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
        embed.set_footer(text="Remember to vote on top.gg! m!vote")
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
        embed.set_footer(text="Remember to vote on top.gg! m!vote")
        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(MinecraftInfo(bot))
