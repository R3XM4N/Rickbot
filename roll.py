import discord
import asyncio

client = discord.Client()
rick = ["roll", "rick", "persona"]


@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    if any(x in message.content for x in rick):
        user = message.author
        file = open("lyricks.txt", "r")
        role = message.guild.get_role(role ID) #add id of the role instead of role ID
        await user.add_roles(role)
        while True:
            line = file.readline()
            if not line:
                break
            elif line == "":
                continue
            await user.send(line)
            await asyncio.sleep(2)

@client.event
async def on_ready():
    print("bot is ready")


client.run('discord token') #put your discord token here
