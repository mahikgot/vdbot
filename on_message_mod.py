import regex
import discord
def role_emoji():
    role_emojie = {
            "viper_pfp" : "Viper",
            "sova_pfp" : "Sova", 
            "sage_pfp" : "Sage",
            "raze_pfp" : "Raze",
            "phoenix_pfp" : "Phoenix",
            "jett_pfp" : "Jett",
            "cypher_pfp" : "Cypher",
            "brimstone_pfp" : "Brimstone",
            "omen_pfp" : "Omen",
            "breach_pfp" : "Breach",
            "reyna_pfp" : "Reyna",
            }
    return role_emojie
def role_embed():
    init_roles = discord.Embed( colour = discord.Colour.teal())
    init_roles.add_field(name = 'Roles', value = 'React to assign your role')
    return init_roles


   

async def hello(message_obj):
    await message_obj.channel.send('Hello!',)

async def motivate(message_obj):
    role_ids = message_obj.role_mentions
    for i in role_ids:
        for j in message_obj.get_role(i):
            for k in j.members:
                await message_obj.channel.send('You can do it <@' + k.id  + '>!')
        
    hold = message_obj.raw_mentions
    for i in hold :
        await message_obj.channel.send('You can do it <@' + i  + '>!')

async def react(message_obj):
    role_emojei = role_emoji()
    holder = []
    emojis = message_obj.channel.guild.emojis
    for i in emojis:
        if i.name in role_emojei.keys():
            holder.append(i)
    for i in holder:
        await message_obj.add_reaction(i)

async def roles(message_obj) :
        init_roles = role_embed()
        message = await message_obj.channel.send(embed = init_roles)
        await react(message)
        return message.id
   

