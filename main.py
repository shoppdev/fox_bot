'''TODO: Moderation, Welcome, Announcer, Cactpot numbers, catagorie policeing (ie photos in photos)
slash commands,  '''

import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)

# bot connects to server
@client.event
async def on_ready():
    # print(f'{client.user} has connected to Discord!')
    
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )
    print('Here to do bot stuff!\n')
    print('\n ~^.^~\n')

# bot responds to messages
@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    print(f'Message from {username}, on channel {channel}, that says: {user_message}')
    
    # check if fox is talking if so dont respond to yourself
    if message.author != client.user:
        
        # fox listen and respond here
        if 'hello' in user_message.lower():
            await message.channel.send(f'Oh, Hi {username}.')
        elif 'goodbye' in user_message.lower() or 'bye' in user_message.lower():
            await message.channel.send(f'See you later {username}!')
        elif 'minty' in user_message.lower() and username != 'fox_name' :
            await message.channel.send('Minty!!!')
        elif 'sad' in user_message.lower():
            await message.channel.send(f'Aww. Chear up {username}.')



client.run(TOKEN)