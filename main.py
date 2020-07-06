import discord
import regex

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    async def hello():
        await message.channel.send('Hello!', tts = True)
    async def motivate():
        if message.mention_everyone :
            for i in message.guild.members :
                await message.channel.send('You can do it <@' + str(i.id)  + '>!', tts = True) 
            return
            
        hold = regex.findall(r'(?<=\<\@\!)(.*?)(?=\>)', message.content)
        for i in hold :
            await message.channel.send('You can do it <@' + i  + '>!', tts = True)
#    async def play():
#    hold = regex.findall(r'(?<=\<\@\!)(.*?)(?=\>)', message.content)
    #insert new row into database containing user ids
    #generate new group id number if have not played together before 

    commands = {
            '$hello' : hello,
            '$motivate' : motivate,
            }

    if message.author == client.user:
        return
    if message.content.split(' ', 1)[0] in commands.keys() :
        await commands[message.content.split(' ', 1)[0]]()



client.run('NzI5Njg0OTI4MTk0Njc0NzU5.XwMjoA.tu0_LuzxcuiuwecBgtF5d5e46o4')


