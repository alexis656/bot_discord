import discord 
from bot_logic import gen_pass

# The intents variable stores the bot's priviliges
intents = discord.Intents.default()
# Enabling the message-reading privelege
intents.message_content = True
# Creating a bot in the client variable and transferring it the priveleges
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('en que puedo ayudar'):
        await message.channel.send("nesesito alluda")
    elif message.content.startswith('lo que tus nos pide no podemos aserlo'):
        await message.channel.send("tarea")
    else:
        await message.channel.send("Your password " + gen_pass(10))

client.run("MTE1NTIwMTc5ODI0MDQ4NTUyNg.Get8ma.0LmSvtbes99z18Y0wdFBEuLuSHaDz3TXaUONp0")
