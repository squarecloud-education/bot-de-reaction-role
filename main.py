import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(".env", override=True)

intents = discord.Intents.all()

bot = commands.Bot("!", intents=intents)

@bot.event
async def on_ready():
    await bot.load_extension("cogs.role_reactions")
    synced = await bot.tree.sync()
    print(f"Bot online como {bot.user}. {len(synced)} comandos sincronizados")

if __name__ == "__main__":
    bot.run(os.getenv("TOKEN"))