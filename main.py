import discord
import on_message_mod

class Vbot(discord.Client):
    
    commands = {
            "$hello" : on_message_mod.hello,
            "$motivate" : on_message_mod.motivate,
            }
    
    async def on_ready(self):
        with open('roles_message_id.txt', 'r') as f:
            self.roles_message_id = int(f.read())
            
        print('We have logged in as {0.user}'.format(self))

    async def on_raw_reaction_add(self, payload):
        if payload.message_id == self.roles_message_id:
            role_name = on_message_mod.role_emoji()[payload.emoji.name]
            guild_roles = payload.member.guild.roles
            
            for i in guild_roles:
                if i.name == role_name:
                    await payload.member.add_roles(i)

    async def on_raw_reaction_remove(self, payload):
        if payload.message_id == self.roles_message_id:
            role_name = on_message_mod.role_emoji()[payload.emoji.name]
            user_id = payload.user_id
            guild = self.get_guild(payload.guild_id)
            member = guild.get_member(user_id)
            guild_roles = member.guild.roles
            
            for i in guild_roles:
                if i.name == role_name:
                    await member.remove_roles(i)
                    
    async def on_message(self, message):
        if message.content.split(' ', 1)[0] in self.commands.keys() :
            await self.commands[message.content.split(' ', 1)[0]](message)
            return
        
        if message.content.split(' ', 1)[0] == "$roles":
            with open('roles_message_id.txt', 'w') as f:
                f.write(str(await on_message_mod.roles(message)))
                
            with open('roles_message_id.txt', 'r') as f:
                self.roles_message_id = int(f.read())
                
bot = Vbot()
bot.run('SECRET')


