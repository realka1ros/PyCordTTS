import discord
import pyttsx3

tts = pyttsx3.init()

rate = tts.getProperty('rate')
tts.setProperty('rate', 200)

volume = tts.getProperty('volume')
tts.setProperty('volume',1.0)
tts.runAndWait()

voices = tts.getProperty('voices')
tts.setProperty('voice', voices[0].id)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    print(f'TTS Volume: {volume}')
    print(f'Rate: {rate}')
    print(f'Voice: {voices}')
    tts.say(f'We have logged in as {client.user}')
    tts.runAndWait()
    tts.stop()

@client.event
async def on_message(message):
    if message.author != client.user:
        text = ' ' * 10 + message.content
        tts.say(text)
        tts.runAndWait()
        tts.stop()

client.run('bot token here')