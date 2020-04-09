import discord
import keep_alive
from discord.ext import commands
import asyncio

import constants as c

recentlyCalled = {}

from dotenv import load_dotenv
load_dotenv()
import os
TOKEN = os.getenv("TOKEN")

bot = commands.Bot(command_prefix='m!', description='Minecraft')
bot.remove_command('help')

support_guild = None


@bot.event
async def on_ready():
    global support_guild
    await bot.change_presence(
        status=discord.Status.dnd,
        activity=discord.Activity(
            name='Mining Diamonds with ' + str(len(bot.guilds)) + ' servers!',
            type=discord.ActivityType.playing))
    print('Logged on')
    print(bot.user.name)
    support_guild = bot.get_guild(c.SERVER_ID)


@bot.event
async def on_message(message):
    # Non-Prefix Commands
    if message.content.lower().startswith('creeper'):
        await message.channel.send('aw man')

    if message.content.lower().startswith('so we back in the mine'):
        await message.channel.send(
            'got our pickaxe swinging from side to side, side, side to side')

    if message.content.lower().startswith('this task a gruelling one'):
        await message.channel.send(
            'hope to find some diamonds to night, night, night diamonds tonight'
        )

    if message.content.lower().startswith('heads up'):
        await message.channel.send('hear a sound, turn around and look up')

    if message.content.lower().startswith('pacer'):
        await message.channel.send('yes')

    if message.content.lower().startswith('i could never forget those eyes'):
        await message.channel.send('COS BABY TONIGHT')

    if message.content.lower().startswith(
            'the creepers tryna steal all our stuff again'):
        await message.channel.send('stuff again, \'gain, \'gain')

    await bot.process_commands(message)


@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title='Minecraft Bot Help Page',
        description='''		
		**Main Commands:**
		m!wiki - gives you a link to the minecraft wiki
		m!blocks - tells you how many blocks there are
		m!servers - servers are epic
		m!senddiamonds - send diamonds to your friends (mention them)
		m!revenge - gives you the lyrics to the popular song
		m!java - information about the java platform
		m!bedrock - information about the bedrock platform
		m!nostalgia - nostalgia that will make you cry
		m!snapshots - information about the newest beta version of minecraft

		**Mob Commands**:
		m!zombie - information about zombies
		m!creeper - so we back in the mine
		m!spider - information about spiders
		m!skeleton - information about skeletons
		m!zombiepigman - information about zombie pigmen
		m!enderdragon - information about the ender dragon
		m!wither - information about the wither
		m!pig - information about the pig
		m!cow - information about cows
		m!sheep - information about sheep

		**Other Commands**:
		m!help - displays this message
		m!server - link to Minecraft Bot Official Server
		m!vote - link to vote page
		m!ping - see how fast im running :runner:
		m!invite - invite minecraft bot to another server

		Minecraft Bot Official Server: https://discord.gg/X6cxXck
		''',
        color=discord.Colour.green())
    embed.set_footer(text='Bot made by matthew#8906 and ( ͡° ͜ʖ ͡°)#0001')
    await ctx.send(embed=embed)


@bot.command()
async def say(ctx, *, message):
    await message.delete()
    await ctx.channel.send(message)


@bot.command()
async def wiki(ctx):
    print(ctx.message.content)
    print(ctx.message.author)
    print(ctx.message.guild)
    print('--------------------------------')
    embed = discord.Embed(
        title='Minecraft Wiki',
        description='https://minecraft.gamepedia.com/Minecraft_Wiki',
        color=discord.Colour.blue())
    await ctx.channel.send(embed=embed)


@bot.command()
async def blocks(ctx):
    print(ctx.message.content)
    print(ctx.message.author)
    print(ctx.message.guild)
    print('--------------------------------')
    await ctx.channel.send('There are more than 150 blocks in minecraft!')


@bot.command()
async def servers(ctx):
    print(ctx.message.content)
    print(ctx.message.author)
    print(ctx.message.guild)
    print('--------------------------------')
    await ctx.channel.send(
        'servers are great and they are the best way to play with friends on minecraft java'
    )


@bot.command()
async def senddiamonds(ctx, member: discord.User):
    print(ctx.message.content)
    print(ctx.message.author)
    print(ctx.message.guild)
    print('--------------------------------')
    await member.send('''Have some diamonds!!!!!!! ** Sent by {0} **
	<:diamond:616316009288040470> <:diamond:616316009288040470> <:diamond:616316009288040470> <:diamond:616316009288040470> <:diamond:616316009288040470> '''
                      .format(ctx.message.author))
    await ctx.send('Sent!')


@bot.command()
async def creeper(ctx):
    print(ctx.message.content)
    print(ctx.message.author)
    print(ctx.message.guild)
    print('--------------------------------')
    embed = discord.Embed(
        title=
        'Creeper <:creeper:616315623219396660> <:creeper:616315623219396660> <:creeper:616315623219396660>',
        description='Aww Man...',
        colour=discord.Colour.green())
    embed.set_image(
        url=
        'https://thumbs.gfycat.com/EntireReflectingKakarikis-size_restricted.gif'
    )
    await ctx.send(embed=embed)


@bot.command()
async def ping(ctx):
    print(ctx.message.content)
    print(ctx.message.author)
    print(ctx.message.guild)
    print('--------------------------------')
    embed = discord.Embed(
        title='Bot Latency',
        description='**{0}**ms'.format(int(bot.latency * 100)),
        colour=discord.Colour.green())
    return await ctx.send(embed=embed)


@bot.command()
async def revenge(ctx):
    print(ctx.message.content)
    print(ctx.message.author)
    print(ctx.message.guild)
    print('--------------------------------')
    await ctx.channel.trigger_typing()
    await ctx.channel.send('https://genius.com/Captainsparklez-revenge-lyrics')


@bot.command()
async def bedrock(ctx):
    print(ctx.message.content)
    print(ctx.message.author)
    print(ctx.message.guild)
    print('--------------------------------')
    await ctx.channel.trigger_typing()
    embed = discord.Embed(
        title='Bedrock is available on:',
        description=
        'Phone and Tablet (Android, IOS, Fire OS, Windows Mobile), Windows 10, Nintendo Switch, Xbox One, PS4, Fire TV and Gear VR. Learn more about Bedrock  at https://minecraft.gamepedia.com/Bedrock_Edition',
        colour=discord.Colour.green())
    await ctx.channel.send(embed=embed)


@bot.command()
async def java(ctx):
    print(ctx.message.content)
    print(ctx.message.author)
    print(ctx.message.guild)
    print('--------------------------------')
    await ctx.channel.trigger_typing()
    embed = discord.Embed(
        title='Java Edition is available on:',
        description=
        'Linux, MacOS and Windows. Learn more about Java Edition  at https://minecraft.gamepedia.com/Java_Edition',
        colour=discord.Colour.green())
    await ctx.channel.send(embed=embed)


@bot.command()
async def nostalgia(ctx):
    print(ctx.message.content)
    print(ctx.message.author)
    print(ctx.message.guild)
    print('--------------------------------')
    await ctx.channel.trigger_typing()
    embed = discord.Embed(
        title='Nostalgia that will make you cry',
        description='https://www.youtube.com/watch?v=MmB9b5njVbA',
        colour=discord.Colour.green())
    await ctx.channel.send(embed=embed)


@bot.command()
async def server(ctx):
    print(ctx.message.content)
    print(ctx.message.author)
    print(ctx.message.guild)
    print('--------------------------------')
    if ctx.guild.id == c.SERVER_ID:
        embed = discord.Embed(
            title='You are already in this server',
            description=
            f'However, you can still invite your friends with this link: {c.SERVER_INVITE}',
            colour=discord.Colour.green())
        embed.set_image(
            url=
            'https://cdn.discordapp.com/attachments/539843161711968278/625373937102094336/d3d41affe02b7c34414883979a5aac52.png'
        )
        return await ctx.send(embed=embed)
    await ctx.channel.trigger_typing()
    embed = discord.Embed(
        title='--> Minecraft Bot Official Server <--',
        colour=discord.Colour.green(),
        url='https://discord.gg/YFnWHsh')
    embed.set_image(
        url=
        'https://cdn.discordapp.com/attachments/539843161711968278/625373937102094336/d3d41affe02b7c34414883979a5aac52.png'
    )
    await ctx.send(embed=embed)


@bot.command()
async def vote(ctx):
    print(ctx.message.content)
    print(ctx.message.author)
    print(ctx.message.guild)
    print('--------------------------------')
    await ctx.channel.trigger_typing()
    embed = discord.Embed(
        title='--> Vote for Minecraft Bot <--',
        colour=discord.Colour.green(),
        url='https://discordbots.org/bot/616308233950199828/vote')
    embed.set_image(
        url=
        'https://cdn.discordapp.com/attachments/539843161711968278/625373937102094336/d3d41affe02b7c34414883979a5aac52.png'
    )
    await ctx.send(embed=embed)


async def change_status():
    while True:
        await asyncio.sleep(600)
        await bot.change_presence(
            status=discord.Status.dnd,
            activity=discord.Activity(
                name='Minecraft with ' + str(len(bot.guilds)) + ' servers!',
                type=discord.ActivityType.playing))
        print('UPDATED STATUS')
        print('--------------------------------')


@bot.command()
async def zombie(ctx):
    print(ctx.message.content)
    print(ctx.message.author)
    print(ctx.message.guild)
    print('--------------------------------')
    embed = discord.Embed(
        title='Zombie',
        description='''
Zombies spawn in groups of 4. They pursue the player on sight from 40 blocks away, as opposed to 16 blocks for other hostile mobs. The detection range of zombies is reduced to half of their normal range (20 blocks) when the player is wearing a zombie mob head.‌[Java Edition only] Zombies periodically make groaning sounds, which can be heard up to 16 blocks away. Zombies attempt to avoid obstacles, including sheer cliffs and lava, and try to find the shortest path toward the player. Unlike skeletons, zombies do not try to avoid being hit, and continue to pursue the player even when being attacked. Zombies can sometimes deal damage through a closed door, as shown in the picture to the right. Zombies sink in water, which facilitates their transformation into drowned.''',
        colour=discord.Colour.green())
    embed.set_image(
        url=
        'https://gamepedia.cursecdn.com/minecraft_gamepedia/thumb/4/42/ZombieInDoor.png/300px-ZombieInDoor.png?version=1cf1c53737551fae1d2df791383f1122'
    )
    await ctx.send(embed=embed)


@bot.command()
async def spider(ctx):
    print(ctx.message.content)
    print(ctx.message.author)
    print(ctx.message.guild)
    print('--------------------------------')
    embed = discord.Embed(
        title='Spider',
        description='''
Spiders are hostile to the player and to iron golems as long as the light level immediately around them is 11 or less; otherwise they do not attack unless provoked. Hostile spiders continue to chase the player even when exposed to well-lit locations. If a spider sustains damage from a source other than a direct attack from the player, such as falling, its hostility is reset.
Spiders can climb up over walls and other obstacles. If a spider cannot find an ideal path to the player (when a player goes behind or on top of a wall), it approaches as close as it can to the player's position from the outside or below, and proceed to climb the wall vertically until it gets to the top, even if it loses its aggression towards the player. Additionally, when a spider loses its aggression on the player, it continues moving forward blindly for about two seconds. This behavior causes the spider to climb up any walls in its path. If a spider tries to go through the world border, it starts climbing the world border instead.''',
        colour=discord.Colour.red())
    embed.set_image(
        url=
        'https://gamepedia.cursecdn.com/minecraft_gamepedia/thumb/8/84/Spider.png/150px-Spider.png?version=f0d20dc8fb4812c9954026abc83fbb08'
    )
    await ctx.send(embed=embed)


@bot.command()
async def skeleton(ctx):
    print(ctx.message.content)
    print(ctx.message.author)
    print(ctx.message.guild)
    print('--------------------------------')
    embed = discord.Embed(
        title='Skeleton',
        description='''
Skeletons chase any player or iron golem they see within 16 blocks. They can climb stairs, navigate mazes, and traverse other complex obstacles to get within shooting range. When they are within 15 blocks of the player with a clear line of sight, they stop chasing and start shooting with arrows, one arrow every 2 seconds (1 on hard difficulty). They can strafe at a player's walking speed in circular patterns to try to dodge attacks during the process, and retreat to safe range if the player comes too close (4 blocks or less) to them. The detection range of skeletons is reduced to half of their normal range (8 blocks) while the player wears a skeleton mob head.

The skeleton's accuracy is based on the difficulty. Skeletons have an "error" of 10 on easy, 6 on normal, and 2 on hard. This is compared to the player's "error" of 1. To account for gravity, skeletons aim 0.2 blocks higher for every block horizontal they are from the target.

If a skeleton's arrow hits certain hostile mobs, that mob attacks the skeleton the same way it would attack the player, if it was not hit by the player first. If a skeleton is attacked by another mob (usually another skeleton), it may attack that mob, reorienting on the player once that mob is dead.

Skeletons sink in water and are unable to swim, but do not drown. They will continue to shoot at the player while underwater, but the water will slow down their arrows.

If spawned with no weapon at all (which can be spawned with /summon skeleton ~ ~ ~ {HandItems:[{id:air,Count:1b}]}), a skeleton acts like a zombie (though faster), coming at the player with arms outstretched and damaging the player by touching them.

Skeletons are also able to climb ladders, but only when forced to, as their AI does not handle ladders in a special way.

Skeletons holding tipped arrows in their offhand always shoot that type of arrow; these arrows are not consumed.''',
    )
    embed.set_image(
        url=
        'https://gamepedia.cursecdn.com/minecraft_gamepedia/thumb/2/23/Skeleton.png/125px-Skeleton.png?version=65b75c40596c1824995eb8bb5180bac0'
    )
    await ctx.send(embed=embed)


@bot.command()
async def zombiepigman(ctx):
    print(ctx.message.content)
    print(ctx.message.author)
    print(ctx.message.guild)
    print('--------------------------------')
    embed = discord.Embed(
        title='Zombie Pigman',
        description='''
Zombie pigmen can spawn in the Nether, from nether portals, or from pigs struck by lightning. They have a 5% chance of spawning as a baby zombie pigman, and a baby zombie pigman has a 5% chance of spawning as a chicken jockey.

All zombie pigmen spawn with a golden sword, which has a small chance of being enchanted. This chance increases at higher difficulties, and the sword's enchantment is usually a higher level.

On Halloween (October 31), zombie pigmen have a 22.5% chance of spawning with a pumpkin or a 2.5% chance of spawning with a jack o'lantern equipped as headgear.‌[JE only]

Zombie pigmen tend to move relatively slowly. They cannot drown and are immune to fire and lava damage. Baby zombie pigmen are faster than adult zombie pigmen. When provoked, their speed increases to the player's walking speed. They also make an aggressive noise between 0 to 39 ticks after they are attacked, upon which they crowd around and try to overwhelm the player. In addition, some zombie pigmen have the ability to spawn reinforcements when attacked (similar to zombies), including when killed in a single hit.

Like zombies and husks, zombie pigmen usually bang on wooden doors, and on Hard difficulty, they can break them.
Some zombie pigmen have the ability to pick up items, including weapons they feel are better than their golden sword, which they drop with the same chance as if killed with Looting I.

Zombie pigmen try to destroy any turtle eggs they see within 23 blocks away, not counting the block they are standing in.

Zombie pigmen are undead mobs, and are damaged by the status effect Instant Health and healed by the status effect Instant Damage. They are unaffected by the status effects Regeneration and Poison. They are ignored by the wither and affected by the Smite Enchantment.''',
        colour=discord.Colour.green())
    embed.set_image(
        url=
        'https://gamepedia.cursecdn.com/minecraft_gamepedia/thumb/0/09/Zombie_Pigman.png/150px-Zombie_Pigman.png?version=e4e4427627095d2a70017d437eeb3beb'
    )
    await ctx.send(embed=embed)


@bot.command()
async def enderdragon(ctx):
    print(ctx.message.content)
    print(ctx.message.author)
    print(ctx.message.guild)
    print('--------------------------------')
    embed = discord.Embed(
        title='Ender Dragon',
        description='''
The ender dragon is a versatile, flying boss mob found when first entering the End. It is the first boss added to Minecraft. It is also the largest mob naturally spawning in the game.

The ender dragon spawns naturally in the End when the first player enters the dimension, and it spawns on any difficulty. In Peaceful, it still fires damaging fireballs, but its body does no damage.

Players can re-summon the ender dragon once the fight is over by placing four end crystals on the edges of the exit portal — one on each side. (Fewer crystals can be used by exploiting this trick.) When the dragon is re-summoned, a series of explosions resets the obsidian pillars, iron bars, and end crystals. The top of each pillar will appear to explode, destroying any player-placed blocks.''',
        colour=discord.Colour.purple())
    embed.set_image(
        url=
        'https://gamepedia.cursecdn.com/minecraft_gamepedia/0/0a/Ender_Dragon.gif?version=747d5fc9faed80f1aea57b0b234bcc85'
    )
    await ctx.send(embed=embed)


@bot.command()
async def wither(ctx):
    print(ctx.message.content)
    print(ctx.message.author)
    print(ctx.message.guild)
    print('--------------------------------')
    embed = discord.Embed(
        title='Wither',
        description='''
		The wither is a powerful, floating undead boss mob that shoots explosive skulls at its enemies, and is currently the only player-made hostile mob in the game.
		
		The wither is spawned by placing 4 blocks of soul sand in a T shape (see image to the left), and putting 3 wither skeleton skulls on top of the three upper blocks. The last block placed must be one of the three skulls, and can be placed by the player or a dispenser. Air blocks are required on either side of the base soul sand block under the upper blocks (keep in mind that "block" refers to any block, not just those that are block shaped; therefore objects such as tall grass and flowers still prevent the Wither from spawning). The building pattern can have any orientation (including horizontal) as well as the skulls. When the wither has completely spawned, it becomes angered and creates an explosion around itself.

    This undead triple-headed creature will then immediately attempt to destroy every living thing in the vicinity, spitting out skulls from each of its three heads and inflicting a creeping corruption on their target, which turns a player’s hearts an unhealthy black. In its fury, the Wither will destroy blocks it comes into contact with - even if you survive the battle, there’s often precious little left standing nearby.

Like other hostile mobs, the wither despawns when the difficulty is changed to Peaceful. The wither spawning structure also fails in Peaceful difficulty; the blocks simply do nothing
''',
    )
    embed.set_image(
        url=
        'https://gamepedia.cursecdn.com/minecraft_gamepedia/thumb/a/aa/Wither.png/250px-Wither.png?version=91949cfe97fe259bf5fda0393e4c4373'
    )
    await ctx.send(embed=embed)


@bot.command()
async def pig(ctx):
    print(ctx.message.content)
    print(ctx.message.author)
    print(ctx.message.guild)
    print('--------------------------------')
    embed = discord.Embed(
        title='Pig',
        description='''
Pigs typically appear the Overworld in groups of 4. They randomly oink.

Pigs move similarly to other passive mobs; they wander aimlessly, and avoid lava and cliffs high enough to cause fall damage. They make no attempt to stay out of water, bobbing up and down to stay afloat. When they encounter obstacles, pigs often hop up and down, apparently attempting to jump over them regardless of whether it is possible. Pigs can be pushed into minecarts and transported by rail.

Pigs follow any player carrying a carrot, carrot on a stick, potato, or beetroot, and stops following if the player moves farther than approximately 8 blocks away from the pig.

When a pig is struck by lightning or hit by a trident with the Channeling enchantment during a thunderstorm, it transforms into a zombie pigman. If the pig was equipped with a saddle, the saddle is lost, and a mounted player is ejected.''',
        colour=discord.Colour.purple())
    embed.set_image(
        url=
        'https://gamepedia.cursecdn.com/minecraft_gamepedia/thumb/2/20/Saddled_Pig.png/150px-Saddled_Pig.png?version=86aec73af77217ee1d10fc0a11fe0557'
    )
    await ctx.send(embed=embed)


@bot.command()
async def cow(ctx):
    print(ctx.message.content)
    print(ctx.message.author)
    print(ctx.message.guild)
    print('--------------------------------')
    embed = discord.Embed(
        title='Cow',
        description=
        '''A cow wanders around, mooing and breathing occasionally. They avoid water, lava and walking off cliffs high enough to cause fall damage. They flee for a few seconds when harmed.

A cow follows a player who holds wheat, but stops following if separated from the player by at least 8 blocks.

If cows are given wheat, they enter love mode and pair off to create calves, granting the player a 1-7 experience orbs. The parent cows have a cooldown of 5 minutes before they can breed again. All babies obtained by breeding take 20 minutes to grow up. The growth of baby cows can be slowly accelerated using wheat; each use takes 10% off of the remaining time to grow up.
''',
        colour=discord.Colour.dark_red())
    embed.set_image(
        url=
        'https://gamepedia.cursecdn.com/minecraft_gamepedia/thumb/8/84/Cow.png/150px-Cow.png?version=0c947ece55d9b6745a416496302a09f9'
    )
    await ctx.send(embed=embed)


@bot.command()
async def sheep(ctx):
    print(ctx.message.content)
    print(ctx.message.author)
    print(ctx.message.guild)
    print('--------------------------------')
    embed = discord.Embed(
        title='Sheep',
        description='''
The majority of sheep are white, with an 81.836% chance of spawning. The light gray, gray and black sheep each have a 5% chance of spawning. Using a spawn egg to get one of these sheep types lies at a reasonable 15%. Brown sheep have an uncommon 3% chance to spawn. Pink sheep have a very rare 0.164% chance of naturally spawning.

5% spawn as babies.‌[Bedrock Edition only]

An adult sheep drops:

1 wool of the corresponding color. Sheep that have not regrown their wool do not drop wool.
1–2 raw mutton (cooked mutton if killed while on fire). The maximum amount is increased by 1 per level of Looting, for a maximum of 1–5 with Looting III.
1–3 experience if killed by a player or tamed wolf.
When sheared, sheep give 1–3 wools and do not take any damage. A sheared sheep regrows its wool after eating from a grass block. Sheep will drop 2-4 wool if hit 8 times with a player's fist and sheared right while being hit for the eighth time.

Sheep also give 1–7 experience after breeding.

Like other baby animals, killing a lamb yields no items nor experience.
''',
        colour=discord.Colour.dark_red())
    embed.set_image(
        url=
        'https://gamepedia.cursecdn.com/minecraft_gamepedia/thumb/6/69/White_Sheep.png/160px-White_Sheep.png?version=a84f92e72ee9341aeea392db587459bc'
    )
    await ctx.send(embed=embed)


@bot.command()
async def invite(ctx):
    print(ctx.message.content)
    print(ctx.message.author)
    print(ctx.message.guild)
    print('--------------------------------')
    await ctx.channel.trigger_typing()
    embed = discord.Embed(
        title='--> Minecraft Bot Invite Link <--',
        colour=discord.Colour.green(),
        url=
        'https://discordapp.com/oauth2/authorize?client_id=616308233950199828&scope=bot&permissions=18432'
    )
    embed.set_image(
        url=
        'https://cdn.discordapp.com/attachments/539843161711968278/625373937102094336/d3d41affe02b7c34414883979a5aac52.png'
    )
    await ctx.send(embed=embed)


@bot.command()
async def snapshots(ctx):
    print(ctx.message.content)
    print(ctx.message.author)
    print(ctx.message.guild)
    await ctx.channel.trigger_typing()
    embed = discord.Embed(
        title='Minecraft Snapshots',
        colour=discord.Colour.green(),
        description='''__Minecraft Java__
		**Snapshot 20w14a**
https://www.minecraft.net/en-us/article/minecraft-snapshot-20w14a
• Hoglins that somehow end up in the Overworld become Zoglins
• Compasses can now be enchanted with Curse of Vanishing
• Strider speed while mounted has been significantly increased
• The main menu background is now in the Nether
• Technical changes and bug fixes

__Minecraft Bedrock__
**Beta 1.16.0.55**
https://feedback.minecraft.net/hc/en-us/articles/360041294872
• Carrot on a stick, Shield, and Shovel now lose durability consistently
• Light propagation now works correctly, fixing hostile mob spawning
• Water can now be collected from Bubble Columns using a bucket 
• Creepers no longer lose aggro immediately after losing sight of its target
• Technical changes and bug fixes''')
    await ctx.send(embed=embed)


@bot.event
async def on_member_join(member):
    if member.guild.id == c.SERVER_ID:
        channel = support_guild.get_channel(c.WELCOME_CHANNEL)
        embed = discord.Embed(
            title=f"Welcome, **{member.nick if not None else member.name}**!",
            description="""
            Welcome to the official **Minecraft Bot support server**.

            You can place your bot suggestions in the <#697360065463713834> channel,
            and can ask for support in the <#697394845140123660> channel.
            """,
            colour=discord.Colour.teal())
        embed.set_thumbnail(url=support_guild.icon_url)
        await channel.send(embed=embed)


keep_alive.keep_alive()

bot.run(TOKEN, bot=True, reconnect=True)
