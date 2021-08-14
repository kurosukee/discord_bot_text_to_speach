import discord
import ffmpeg
import os
from discord.ext import commands
from os import getenv
from gtts import gTTS

bot = commands.Bot(command_prefix='!')
voice_client = None

@bot.event
async def on_ready():
    print('ログインしました。')

@bot.command()
async def join(ctx):
    vc = ctx.author.voice
    if vc is None:
        await ctx.channel.send('ボイチャ繋がってないわよ')
        return
    else:
        await vc.channel.connect()
        return

@bot.command()
async def bye(ctx):
    vc = ctx.voice_client
    if vc is None:
        await ctx.channel.send('ボイチャにいないわよ')
        return
    else:
        await vc.disconnect()

@bot.event
async def on_message(message):
    if message.content.startswith('!'):
        await bot.process_commands(message)
        return
    if message.content == 'うー':
        await message.channel.send('にゃー')
        return
    vc = message.guild.voice_client
    if vc == None:
        return
    else:
        tmpfile = str(message.id) + '.mp3'
        tts = gTTS(text=message.content, lang='ja')
        tts.save(tmpfile)
        source = discord.FFmpegPCMAudio(tmpfile)
        vc.play(source)
        while vc.is_playing():
            continue
        try:
            os.remove(tmpfile)
        except OSError as e:
            return

bot.run(getenv('BOT'))