import configparser
import discord


class Client(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)


config = configparser.ConfigParser()
config.read('config.ini')
token = config['TOKEN']['token']
client = Client()
client.run(token)
