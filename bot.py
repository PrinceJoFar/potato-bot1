import discord
from discord.ext import commands
import asyncio
from itertools import cycle

client = commands.Bot(command_prefix = '.')

client.remove_command('help')

status = ['¯\_(ツ)_/¯', 'R.I.P. Blossom', 'My prefix is "."', 'Drawing Pyus', 'Potato evolved into Fries', 'Preparing Bento']

staffID = "454433275029487626"

#Background Task
async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)


    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(90)

#Login
@client.event
async def on_ready():
    print ("Starting up...")
    print ("Loading...")
    print ("Welcome to The Potato Sack!")
    print ("Please enter a username and password.")
    print ("Username: PotatoBot#4443")
    print ("Password: *********")
    print ("Logging in...")
    print ("Please select a function")
    print ("[1] Start bot")
    print ("[2] Change User")
    print ("[3] Logout")
    print ("Selecting option [1] Start bot.")
    print ("Starting...")
    print ("Connecting...")
    print ("Bot Online")
    print ("--------------------")

#Help
@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    await client.say("Ok. We have sent your the info.")

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.set_author(name='Help')
    embed.add_field(name='.htu', value='How to use!', inline=False)
    embed.add_field(name='.prefix', value='Checks prefix', inline=False)
    embed.add_field(name='.info', value='Displays bot info', inline=False)
    embed.add_field(name='.invite', value='Gives you an invite', inline=False)
    embed.add_field(name='.ping', value='Pong!', inline=False)
    embed.add_field(name='.help', value='Shows this message', inline=False)
    embed.add_field(name='.pyuinfo', value='Displays all of our current Pyu Info', inline=False)
    embed.add_field(name='.adminhelp', value='Shows admin commands', inline=False)
    


    await client.send_message(author, embed=embed)

#Admin Help
@client.command(pass_context=True)
async def adminhelp(ctx):
    message = ctx.message
    channel = ctx.message.channel
    if staffID in [role.id for role in message.author.roles]:
        author = ctx.message.author

        embed = discord.Embed(
            colour = discord.Colour.blue()
        )

        embed.set_author(name='Admin Commands')
        embed.add_field(name='.clear', value='Clears x amount of messages from 2-100', inline=False)
        embed.add_field(name='.displayhelpinfo', value='Displays Help info in chat instead of a DM', inline=False)
        await client.send_message(author, embed=embed)
    
    else:
        await client.send_message(channel, adminDeny)


#Premade Messages
newMemberMessage = """
Hello!

Welcome to The Potato Sack

Make sure to read da rules! 
"""

HowToUse = """
__**How to use**__
For a list of commands type .Help
"""

PyuInfo = """
__**Pyu Info**_

Pyus must always be blushing.
Pyus are a variety of different colors, explore what color ranges you want your Pyu to be!
Never make porn of pyus, for the love of god, they don't even have genitals.
Pyus are around snail sized, and they grow to around bird size when older.
They have magical abilities, depending on what their coloring is.
Pyus shells are venomous when agitated, and can go through even the deepest materials.
Pyus are only one color, in different tones.
Pyus are babies for 5 years of their life, and adults for 20 years. They can live up to 100+ years old.
They have 3 different body types, https://ladybuddygaming.deviantart.com/art/Pyu-Body-Types-751153322
Pyus like being petted on their shells, when they aren't upset or agitated.
Pyus repopulate by merging their slimey bodies and finding a temporary shell, which becomes the child's shell once it is born.
Pyu's gender difference is the orientation of the swirl on the shell, Girls have a swirl going up, boys have a swirl going down.
They appear to hide in their shells, but in reality, their body turns into the slimey 'legs', making them bigger in size.
Pyus try to eat everything they possibly can when hungry.
"""

adminDeny = "**LOL!** Haha funny joke no just don't even try."

#Autorole and Join
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='ツHuman Beansツ')
    await client.add_roles(member, role)
    print ("User " + member.name + " has joined the server")
    await client.send_message(member, newMemberMessage)
    print ("newMemberMessage has been sent to " + member.name)
    
#-Commands-#
    
#Ping
@client.command()
async def ping():
    await client.say('Pong!')

#How to use
@client.command()
async def htu():
    await client.say(HowToUse)

#Prefix
@client.command()
async def prefix():
    await client.say('My current prefix is **"."**')

#Info
@client.command()
async def info():
    await client.say("Hi, I'm @Potato Bot! I am currently a work in progress by @PrinceJoFar#6906. If you have any questions or suggestions please DM @PrinceJoFar#6906 with your ideas or concerns. __**This bot is only for The Potato Sack you will not be able to invite it on any other server**__")    

#Invite
@client.command()
async def invite():
    await client.say('Here ya go! https://discord.gg/e8DMepj')

#Ping
@client.command()
async def pyuinfo():
    await client.say(PyuInfo)
                   
#Clear   
@client.command(pass_context=True)
async def clear(ctx, amount=100):
    message = ctx.message
    channel = ctx.message.channel
    messages = []
    if staffID in [role.id for role in message.author.roles]:
        async for message in client.logs_from(channel, limit=int(amount)):
            messages.append(message)
        await client.delete_messages(messages)
        await client.say('Messages Deleted')
    else:
        await client.send_message(channel, adminDeny)

#Display Help
@client.command(pass_context=True)
async def displayhelpinfo(ctx):
    message = ctx.message
    channel = ctx.message.channel
    if staffID in [role.id for role in message.author.roles]:
        embed = discord.Embed(
            colour = discord.Colour.blue()
        )

        embed.set_author(name='Help')
        embed.add_field(name='.htu', value='How to use!', inline=False)
        embed.add_field(name='.prefix', value='Checks prefix', inline=False)
        embed.add_field(name='.info', value='Displays bot info', inline=False)
        embed.add_field(name='.invite', value='Gives you an invite', inline=False)
        embed.add_field(name='.ping', value='Pong!', inline=False)
        embed.add_field(name='.help', value='Shows this message', inline=False)
        embed.add_field(name='.pyuinfo', value='Displays all of our current Pyu Info', inline=False)
        embed.add_field(name='.adminhelp', value='Shows admin commands', inline=False)

        await client.say(embed=embed)

    else:
        await client.send_message(channel, adminDeny)

client.loop.create_task(change_status())   
client.run(process.env.BOT_TOKEN)
