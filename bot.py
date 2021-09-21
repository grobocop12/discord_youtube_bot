from discord import Message, Member, VoiceChannel, VoiceClient, FFmpegPCMAudio
from discord.ext import commands

from basic_voice import YTDLSource

bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print('Logged on as', bot.user)


@bot.command()
async def test(ctx):
    message: Message = ctx.message
    await message.reply(content='test')


@bot.command()
async def join(ctx: commands.context.Context):
    author: Member = ctx.author
    channel: VoiceChannel = author.voice.channel
    if channel is not None:
        await channel.connect()
    else:
        await ctx.message.reply('Join voice channel and try again')


@bot.command()
async def leave(ctx: commands.context.Context):
    client: VoiceClient = ctx.voice_client
    if client is not None:
        await client.disconnect()


@bot.command()
async def play(ctx: commands.context.Context, url: str):
    client: VoiceClient = ctx.voice_client
    if client is not None:
        filename = await YTDLSource.from_url(url, loop=bot.loop, stream=True)
        client.play(filename)
        pass
