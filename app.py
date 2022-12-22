import discord, time, sys
from discord.ext import commands

bot = commands.Bot(";", self_bot=True)

NAME = "NAME"#discord name with tag
TOKEN = "TOKEN"
active = False
replied = []

@bot.event
async def on_ready():
    print("Locked and loaded!")

@bot.event
async def on_message(message):
    global active, replyList
    if str(message.channel.type) == "private" or str(message.channel.type) == "group":
        if NAME != str(message.author):
            if active == True:
                if message.author not in replied:
                    await message.channel.send("edit this to your liking")
                    replied.append(message.author)
    else:
        await bot.process_commands(message)
        if message.content.split(" ")[0] == ";afk":
            await message.delete()

@bot.command()
async def afk(ctx, option=None):
    global active, replied
    status = discord.Embed(title="bot status", color=discord.Colour(value=11735575))
    if option != None:
        if option.upper() == "ON":
            status.add_field(name="BOT-Reply", value="ON")
            active = True
        if option.upper() == "OFF":
            status.add_field(name="BOT-Reply", value="OFF")
            active = False
        if option.upper() == "RESTART":
            status.add_field(name="BOT-Reply", value="Restarting...")
            replied = []
            status.add_field(name="BOT-Reply", value="Restarted")
    else:
        status.add_field(name="BOT-Reply", value=";afk on / ;afk off / ;afk restart")