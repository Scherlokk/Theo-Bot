import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTI5Mzk2MzM0NjgxMDM3MjIxNw.GA_k3v.Wg11gVMfu9UkfwX-LWYGcTFTxlmipcgq21m1kA')

async def on_message(self, message):
    if message.author == self.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello World!')

async def on_mute(self):
    if discord.on_voice_state_update("t-o", None, discord.self_mute):
        await discord.move_to("Von Eltern belästigt",reason=None)