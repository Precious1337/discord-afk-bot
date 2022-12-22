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
