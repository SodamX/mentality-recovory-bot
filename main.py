import discord
import asyncio
import random

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  async def message(games):
    await client.wait_until_ready()
    while not client.is_closed():
        for game in games:
            await client.change_presence(status = discord.Status.idle, activity = discord.Game(game))
            await asyncio.sleep(10)
  await message(["mentality-recovory-bot", "멘탈 복구봇입니다!"])

@client.event
async def on_message(message):
    if message.content.startswith("!복구"):
        embed = discord.Embed(title="[ 복구 ]", description="멘탈 복구 성공!", color=0xfead67)
        embed.set_image(url=random.choice(["https://cataas.com/cat", "https://cataas.com/cat/cute", "https://cataas.com/cat/gif"]))
        await message.channel.send(embed=embed)

client.run("token")