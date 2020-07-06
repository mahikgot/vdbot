import discord
import on_message_mod
client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):



    if message.author == client.user:
        return
    if message.content.split(' ', 1)[0] in on_message_mod.commands.keys() :
        await on_message_mod.commands[message.content.split(' ', 1)[0]](message)



client.run('NzI5Njg0OTI4MTk0Njc0NzU5.XwMjoA.tu0_LuzxcuiuwecBgtF5d5e46o4')


