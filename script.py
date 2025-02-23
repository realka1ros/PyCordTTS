import discord
import pyttsx3

#Setting Variables for Easier Calling
tts = pyttsx3.init()

client = discord.Client(intents=intents)

#Text to Speech Configuration
rate = tts.getProperty('rate')
tts.setProperty('rate', 200)

volume = tts.getProperty('volume')
tts.setProperty('volume',1.0)
tts.runAndWait()

voices = tts.getProperty('voices')
tts.setProperty('voice', voices[0].id)

intents = discord.Intents.default()
intents.message_content = True

#When the bot is connected and ready
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    print(f'TTS Volume: {volume}')
    print(f'Rate: {rate}')
    print(f'Voice: {voices}')
    tts.say(f'We have logged in as {client.user}')
    tts.runAndWait()
    tts.stop()

#When the bot detects a message
@client.event
async def on_message(message):
    #If the message author IS NOT the bot it will say the message
    if message.author != client.user:
        text = ' ' * 10 + message.content
        tts.say(text)
        tts.runAndWait()
        tts.stop()

client.run('bot token here') #<--------- BOT TOKEN GOES RIGHT HERE
