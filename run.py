"""
This module is the automated poster to discord.
This module will post to the discord whenever the script is run, detailing the callouts for the current raid for the next seven days.
This automation will be run on a daily basis, through a cron job + docker.

@author: Gabriella 'contrastellar' Agathon
"""
import argparse
import discord


DATABASE_CONN = None

intents = discord.Intents.default()
intents.message_content = True
intents.guild_messages = True
intents.presences = False

client = discord.Client(intents=intents)

NUMBER_OF_DAYS = 7

parser: argparse.ArgumentParser = argparse.ArgumentParser(prog='callouts aux',
                        description='The poster for the callouts bot functionality')

parser.add_argument('token')
parser.add_argument('guild_id', type=int)
parser.add_argument('channel_id', type=int)

args: argparse.Namespace = parser.parse_args()

@client.event
async def on_ready():
    print(f'{client.user} has connected.')
    print(args.guild_id)
    guild: discord.Guild = client.get_guild(args.guild_id)
    channel: discord.TextChannel = guild.get_channel(args.channel_id)
    output = 'https://media.discordapp.net/attachments/849035333220040757/1345056174193512529/Tumblr_l_326282912745700.jpg?ex=67c328ad&is=67c1d72d&hm=7e81f9b807e812023eee9bc43ce4e8a588c0aa93db5c7296a86fb15a1a4c3036&=&format=webp&width=550&height=158'
    await channel.send(output)
    await client.close() # Another way to exit, a little bit cleaner than exit(0)
    return

TOKEN = open(args.token, encoding='utf-8').read()
client.run(TOKEN)
