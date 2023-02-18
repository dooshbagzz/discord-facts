import discord
import wikipedia
import random

client = discord.Client()
wikipedia.set_lang("en")

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user.mentioned_in(message):
        page = wikipedia.random(pages=1)
        summary = wikipedia.summary(page)
        fact = summary.split('.')[0] + '.'
        await message.channel.send(fact)

client.run('YOUR_DISCORD_BOT_TOKEN_HERE')
