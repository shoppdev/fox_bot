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
    print('\n ~^.^~\n')
    print('Here to do bot stuff!\n')

    print("I'm connected to these guilds:")
    for guild in client.guilds:
        print(guild)

    # print(
    #     f'{client.user} is connected to the following guild:\n'
    #     f'{guild.name}(id: {guild.id})\n'
    # )
    
    


# bot responds to messages
@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]    # break down usernames to look better printed out (drop the #0000)
    channel = str(message.channel.name)             # grab the channel name
    user_message = str(message.content)             # grab the user message

    # print(f'Message from {username}, on channel {channel}, that says: {user_message}')
    
    # check if fox is talking if so fox dosent respond to themself
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
        elif 'help' == user_message[0]:
            await message.channel.send('I will soon list some help stuff here.')


client.run(TOKEN)