import os
import asyncio
import discord
import random
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

from sys import exit as exit_script

bot_secret_file = "bot_secret.txt"

bot = commands.Bot(command_prefix = '.')

def get_secret():

    # Allow fuction to access variable
    global bot_secret_file

    # Check if the file even exists before trying to open it.
    if os.path.isfile( bot_secret_file ):

        # Open the file.
        f = open( bot_secret_file, "r" )

        # Make sure the file was opened in READ mode.
        if f.mode == "r":

            data = f.read()

            # Dirty way to clean output, I know.

            data = data.replace( "\n", "" )
            data = data.replace( "\t", "" )
            data = data.replace( " ", "" )

            if len( data ):

                return data
            
            else:

                print( "Bot secret file is empty!" )
                exit_script( 1 )

        # Show error and close if file is not in READ mode.
        else:

            print( "Bot secret file wasn't opened in read mode! Aborting ..." )
            exit_script( 1 )

    # Show error and exit if file is not found.
    else:

        print( f"Bot secret file not found! Please make a file named {bot_secret_file} in the same directory as this script with your secret!" )
        exit_script( 1 )


@bot.command()
async def ping(ctx):
    await ctx.send(f'> Pong! {round(bot.latency * 1000)}ms')

@bot.command()
async def ding(ctx):
    await ctx.send('dong ')


@bot.command()
async def meme(ctx):                                                           #this function
    file_path = 'memes/'
    picture_names = os.listdir(file_path)
    await ctx.send(file=discord.File(file_path + random.choice(picture_names)))

@bot.command()
async def clean(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send('> Chat Cleaned!')

@bot.command()
async def be(ctx):
    await ctx.send(">me")

@bot.event
async def on_ready():
    print('%s %s is online' % (bot.user.name,bot.user.id))  

@bot.command()
async def fuck(ctx):
    fuck = """
 ```
 H
　 O
　　 O
　　　 o
　　 　　o
　　　 　    o
　　　　　o
　　　　 。
　　　 。
　　　.
　　　.
　　　 .
　　　　LY SHIT (╯°□°）╯︵ ┻━┻
```
    """
    await ctx.send(fuck)

@bot.command()
async def say(ctx, *, message: commands.clean_content()):
    '''I say what you want me to say. Oh boi...'''
    try:
        await ctx.message.delete()
    except discord.Forbidden:
        pass
    finally:
        await ctx.send(message)    

@bot.command()
async def test(ctx):
    """Allow my bot to join the hood. YOUR hood."""
    em = discord.Embed(color=ctx.author.color, title="test")
    em.description = "test message"
    em.set_footer(text=f"Requested by: {str(ctx.author)}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=em)
 
@client.command()
@commands.has_any_role("Dev","Private")
async def addMember(ctx, member : discord.Member = None, *,reason=None):
    await ctx.message.delete()
    role = get(member.guild.roles, name="Member")
    await member.add_roles(role)

@client.command()
@commands.has_any_role("Dev","Private")
async def removeMember(ctx, member : discord.Member = None, *, reason=None):
    await ctx.message.delete()
    role = get(member.guild.roles, name="Member")
    await member.remove_roles(role)
    channel = await ctx.author.create_dm()
    await channel.send(f'Removed role of Member from {member.name}')




# @bot.event
# async def on_raw_message_delete(raw_message):
#     """Deleted Messages log."""
#     if not raw_message.cached_message:
#         guild = bot.get_guild(raw_message.guild_id)
#         channel = bot.get_channel(raw_message.channel_id)
#         message = await channel.fetch_message(raw_message.message_id)
#     else:
#         message = raw_message.cached_message
#     # if not message.author.bot:  
#         em = discord.Embed(color=message.author.color, title=f":wastebasket: Message Deleted in {channel.id} for {message.author.name} ({message.author.id})")
#         em.description = f"{message.content}"
#         em.set_footer(text=f"Requested by: {str(message.author)}", icon_url=message.author.avatar_url)
#         await bot.get_guild(669119687530905610).get_channel(670895452547317777).send(embed=em)
#     print(f'Message deleted in {raw_message.channel.id}')    


@bot.event
async def on_message_delete(message):
    """Deleted Messages log."""
    # if not message.author.bot:  
    # await bot.get_guild(669119687530905610).get_channel(669372334616084520).send(f""":wastebasket: {message.author.name} ({message.author.id}) message deleted in #{message.channel.name}:```{message.content}```""")
    em = discord.Embed(color=message.author.color, title=f":wastebasket: Message Deleted in {message.channel.name}")
    em.description = f"View: {message.channel.mention}\n```{message.content}```"
    em.set_footer(text=f"Sender: {str(message.author)} ( {message.author.id} )", icon_url=message.author.avatar_url)
    await bot.get_guild(669119687530905610).get_channel(670895452547317777).send(embed=em)
    print(f'Message deleted in {message.channel.name}')   


try: 

    bot.run( get_secret() )

except discord.errors.LoginFailure as error:

    print( f"Error logging in! Error: {error}" )