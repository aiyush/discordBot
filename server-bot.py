import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f"Logged in as {client}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!register"):
        await message.channel.send("You are now a registered member of this server!")

    if message.content.startswith("!admin"):
        await message.channel.send(f"You are now an admin of this server!")


    if message.content.startswith("!hello"):
        author = message.author.mention
        await message.channel.send(f"Hello {author}.How are you!")


async def on_member_join():
    print(f"Welcome to your coding Xanadu buddy.Strap on to your seat and plug in those headphones...coz itz CODING TIME!!!!")


client.run("LqMyMLLM1ODz3Nzc3ODE3DzEx.XXkaJJ8F3LxFFmg.D5K5H6cuG3O3_nKDPOf6k_9a45gL")