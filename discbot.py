import discord
import asyncio
import config
from random import randint

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

@client.event
async def on_message(message):
    if message.content.startswith('!cat'):
        cats = []
        cats.append('./res/img/cat1.jpg')
        cats.append('./res/img/cat2.jpg')
        cats.append('./res/img/cat3.jpg')
        
        num = randint(0,2)
        await client.send_file(message.channel, cats[num])

if __name__=="__main__":
    client.run(config.Mzc5MDQ2OTUzMTMwMDAwMzg0.DOwW_g.ntaG2QvK450g0a-US9KuhsGa_u0)
