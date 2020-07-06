import regex

commands = {
        '$hello' : on_message_mod.hello,
        '$motivate' : on_message_mod.motivate,
        }
def get_mention_id(text) :
   return regex.findall(r'(?<=\<\@\!)(.*?)(?=\>)', text)

async def hello(message_obj):
    await message_obj.channel.send('Hello!', tts = True)
async def motivate(message_obj):
    if message_obj.mention_everyone :
        for i in message_obj.guild.members :
            await message_obj.channel.send('You can do it <@' + str(i.id)  + '>!', tts = True) 
        return
        
    hold = get_mention_id(message_obj.content)
    for i in hold :
        await message_obj.channel.send('You can do it <@' + i  + '>!', tts = True)
