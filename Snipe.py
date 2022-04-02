#made by @Lotus.pyc on instagram (:

import asyncio
import discord
import colorama
import sys
import os
from colorama import Fore
from discord.ext import commands
from discord.errors import Forbidden

def Clear():
   if sys.platform == "linux":
    os.system("clear")
   elif sys.platform == "win32":
    os.system("cls")
Clear()

print(f'''
                       {Fore.RED}╔═══════════════════════════════════════════════╗
                       {Fore.RED}║                                               ║
                       {Fore.RED}║  {Fore.BLUE}██╗  ██╗ █████╗ ██████╗ ███╗   ███╗ █████╗   {Fore.RED}║
                       {Fore.RED}║  {Fore.CYAN}██║ ██╔╝██╔══██╗██╔══██╗████╗ ████║██╔══██╗  {Fore.RED}║
                       {Fore.RED}║  {Fore.BLUE}█████╔╝ ███████║██████╔╝██╔████╔██║███████║  {Fore.RED}║
                       {Fore.RED}║  {Fore.CYAN}██╔═██╗ ██╔══██║██╔══██╗██║╚██╔╝██║██╔══██║  {Fore.RED}║
                       {Fore.RED}║  {Fore.BLUE}██║  ██╗██║  ██║██║  ██║██║ ╚═╝ ██║██║  ██║  {Fore.RED}║
                       {Fore.RED}║  {Fore.CYAN}╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝  {Fore.RED}║
                       {Fore.RED}║  {Fore.CYAN}Snipe Bot                                    {Fore.RED}║
                       {Fore.RED}║                                               ║ 
                       {Fore.RED}╚═══════════════════════════════════════════════╝

                        {Fore.RED}Karma Instagram: {Fore.GREEN}@karma.ngo_
                        {Fore.RED}Creator Instagram: {Fore.BLUE}@Lotus.pyc
                        {Fore.RED}Creator Discord: {Fore.GREEN}Lotus#8986

''')

colorama.init()
intents = discord.Intents.all()
Karma = discord.Client()
Karma = commands.Bot(
    description='snipe',
    command_prefix=".",
    reconnect=True
)
Karma.remove_command('help') 

smc = None
sma = None
smid = None

@Karma.event
async def on_message_delete(message):

    global smc
    global sma
    global smid

    smc = message.content
    sma = message.author.id
    smid = message.id
    await asyncio.sleep(60)

    if message.id == smid:
        sma = None
        smc = None
        smid = None

@Karma.command()
async def snipe(message):
    if smc==None:
        await message.channel.send("There are no recently deleted messages")
    else:
        embed = discord.Embed(description=f"{smc}")
        embed.set_footer(text=f"Snipe by: {message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
        return


Karma.run('BOT-TOKEN-HERE')
