import discord
import random
import requests 
import json
from pprint import pprint

TOKEN='OTE0NTczNTc4Nzk4NzY0MDQy.YaPBBQ.pYdWRn6QXLK82aFIbzURxDCqogc'

command_prefix1='all.'
command_prefix2='partofspeech.'

client=discord.Client()

@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

@client.event

async def on_message(message):
    try:
        if message.author!=client.user and message.content.startswith(command_prefix1):
            word1=message.content.replace(command_prefix1, '')
            word=str(word1).lower()
            url1=f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
            response= requests.get(url1).json()
            
            for meaning in response[0]['meanings'] :
                output=''
                output+='definition:'+meaning['definitions'][0]['definition']+'\n'
                if(meaning['definitions'][0]['antonyms']) :
                    output+='antonyms:'+str(meaning['definitions'][0]['antonyms'])+'\n'
                if(meaning['definitions'][0]['synonyms']) :
                    output+='synonyms:'+str(meaning['definitions'][0]['synonyms'])+'\n'
                output+='example:'+meaning['definitions'][0]['example']+'\n'
                output+='partofspeech:'+ meaning['partOfSpeech']
                await message.channel.send(output)
        
            response='origin:'+response[0]['origin']
            await message.channel.send(response)
        
        elif message.author!=client.user and message.content.startswith(command_prefix2):
            word1=message.content.replace(command_prefix2, '')
            word=str(word1).lower()
            url1=f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
            response= requests.get(url1).json()
            output='partofspeech:'
            for meaning in response[0]['meanings']:
                output+=meaning['partOfSpeech']+','
            output=output[:-1]
            await message.channel.send(output)
    except:
        await message.channel.send('word you entered is not found in the dictionary')


client.run(TOKEN)


