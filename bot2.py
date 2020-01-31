import os
import asyncio
import discord
import random
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
    
from bot_secret import get_secret
from discord.utils import get

client_ = discord.Client()
client = commands.Bot(command_prefix = '!')

import sys
try:
    if sys.argv[1] != "sc":
        print("you need to start with the shell of batch script")
        exit(1)
except IndexError:
    print("you need to start with the shell of batch script")
    exit(1)
@client.event
async def on_ready():
    client.load_extension("cogs.user_info")
    client.load_extension("cogs.faq")
    client.load_extension("cogs.badwords")
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Leaking salc\'s base in progress'))
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_memeber_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_memeber_remove(member):
    print(f'{member} has left the server.')

#Ping Command (Ex: Pong! 93ms)
@client.command()
async def ping(ctx):
    await ctx.send(f'> Pong! {round(client.latency * 1000)}ms')

@client.command()
@commands.has_any_role("Moderator","Private Chat Access","Administrator")
async def addmember(ctx, member : discord.Member = None, *,reason=None):
    #await ctx.message.delete()
    role = get(member.guild.roles, name="Member")
    await member.add_roles(role)
    await ctx.send(f'> Added member role for {member.name}')


@client.command()
@commands.has_any_role("Moderator","Private Chat Access","Administrator")
async def removemember(ctx, member : discord.Member = None, *, reason=None):
    #await ctx.message.delete()
    role = get(member.guild.roles, name="Member")
    await member.remove_roles(role)
    await ctx.send(f'> Removed member role for {member.name}')

@client.command()
@commands.has_any_role("Moderator", "Administrator")
async def restart(ctx):
    exit(69) # this shoudld restart the bot if its started with start.sh

badwords = ["nigger", "faggot", "pornhub.com"]    
    
@client.event
async def on_message(message):
	if any(word in message.content.lower() for word in badwords):
		### Print log in console:
		print('Removed message - %s : %s' % (message.author, message.content))
		### Remove the message which triggered the bot
		await message.delete()
		### Send reply/notification

## ----------------------------------- DONT EDIT PAST THIS LINE UNLESS YOU KNOW WHAT YOU'RE DOING! --------------------------------------------
if __name__ == "__main__": # only run bot if this file wasn't imported
    try: 
        client.run( get_secret() )
    except discord.errors.LoginFailure as error:
        print( f"Error logging in! Error: {error}" )
