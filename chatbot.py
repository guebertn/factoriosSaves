apikey = 'MTA5OTE0NDA1OTc2MDY4OTE1Mg.GR3AUS.XKnh3fIKJfg6xWcQp5M2efdP78L-dyq_YM5JSI'


import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await channel.send("logged in")

async def post_message():
    channel = client.get_channel(YOUR_CHANNEL_ID) # Replace with the ID of the channel you want to post to
    await channel.send("Hello, World!") # Replace "Hello, World!" with your desired message
    
async def post_message_periodically():
    while True:
        await post_message()
        await asyncio.sleep(300 + 300*random.random()) # Waits for 5-10 minutes before posting again

client.loop.create_task(post_message_periodically())
client.run('MTA5OTE0NDA1OTc2MDY4OTE1Mg.GR3AUS.XKnh3fIKJfg6xWcQp5M2efdP78L-dyq_YM5JSI') # Replace with your bot's token