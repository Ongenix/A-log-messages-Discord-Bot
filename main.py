import discord, os
from discord.ext import commands

intents = discord.Intents.default();intents.message_content = True;bot = commands.Bot(
	command_prefix="!",
	case_insensitive=True,
  intents=intents
);bot.author_id = 0

#########################
token = ""
#########################

@bot.event
async def on_message(ctx):
  with open("messages.txt","a") as f:
    message = ctx.content
    if len(open("messages.txt","r").readlines())>0:
      f.write(f"\n{ctx.author} - {message}")
    else:
      f.write(f"{ctx.author} - {message}")

if os.getenv("token") != None:
  bot.run(os.getenv("token"))
else:
  bot.run(token)
