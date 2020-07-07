import discord
import on_message_mod

class Vbot(discord.Client):
    commands = {
            "$hello" : on_message_mod.hello,
            "$motivate" : on_message_mod.motivate,
            }
    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self))

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.split(' ', 1)[0] in self.commands.keys() :
            await self.commands[message.content.split(' ', 1)[0]](message)
bot = Vbot()
bot.run('NzI5Njg0OTI4MTk0Njc0NzU5.XwMjoA.tu0_LuzxcuiuwecBgtF5d5e46o4')


