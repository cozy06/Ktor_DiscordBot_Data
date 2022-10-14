import os

import discord
from discord.ext import commands

project_path = os.getcwd()

token = open(project_path + "/TOKEN.txt", 'r')
TOKEN = token.readline()
token.close()

Default_Channel_ID = 972220280376262696

intents = discord.Intents.all()
bot_activity = discord.Game(name='git 수정 중')
help_command = 'fd'
bot = commands.Bot(intents=intents, command_prefix='$', help_command=None, activity=bot_activity)


@bot.event
async def on_ready():
    print(f'Login bot: {bot.user} {bot.application_id}')


@bot.command()
async def getpermission(ctx):
    PlayerID = str(ctx.message.author.id)
    PlayerName = str(ctx.message.author)
    path = project_path + "/DATA"
    if not os.path.isdir(path):
        os.mkdir(path)
        print(f'Making {path}')

    elif os.path.isdir(path) and not os.path.isfile(path + "/" + PlayerID + "_DATA.TXT"):
        f = open(path + "/" + PlayerID + "_DATA.TXT", 'w')
        f.write('PlayerName:\\' + PlayerName + '\nmoney:\\10000')
        f.close()
        print(f'Making {path + "/" + PlayerName + "_DATA.TXT"}')
        role = discord.utils.get(ctx.message.guild.roles, name="player")
        await ctx.message.author.add_roles(role)
        await ctx.send("```diff\n- 서버 규칙을 잘 지켜주세요 -\n``````fix\n1.--\n2.--\n```")
        await ctx.channel.send('`added role "player" to ' + PlayerName + '`')

    # elif os.path.isfile(path + "/" + PlayerID + "_DATA.TXT"):
    #     f = open(path + "/" + PlayerID + "_DATA.TXT", 'a')
    #     f.write('\n' + PlayerName)
    #     print(f'Writing in {PlayerID}_DATA.TXT')
    #     role = discord.utils.get(ctx.message.guild.roles, name="player")
    #     await ctx.message.author.add_roles(role)
    #     await ctx.channel.send('added role "player" to ' + PlayerName)
    #     await ctx.send("서버 규칙을 잘 지켜주세요\n> 1.--\n> 2.--")


@bot.command()
async def communicate(ctx, arg1):
    await ctx.send("sending " + arg1 + "...")
    path = project_path + "/DATA/ConnectionJava"
    filepath = project_path + "/DATA/ConnectionJava/todo.txt"
    if not os.path.isdir(path):
        os.mkdir(path)
        f = open(filepath, 'w')
        f.write("PlayerID:\\" + str(ctx.message.author.id) + "\ntodo:\\" + str(arg1))
        f.close()

    elif not os.path.isdir(filepath):
        f = open(filepath, 'w')
        f.write("PlayerID:\\" + str(ctx.message.author.id) + "\ntodo:\\" + str(arg1))
        f.close()
    await ctx.send("sent " + arg1)




@bot.command()
async def add(ctx, arg1):
    if str(arg1) == "money":
        player_roles = [y.name.lower() for y in ctx.message.author.roles]
        if "admin" in player_roles:
            await ctx.send("money added")

        else:
            await ctx.send("have no permission")


# @bot.command()
# async def playerID(ctx, arg1):
#     player_roles = [y.name.lower() for y in ctx.message.author.roles]
#     if "admin" in player_roles:
#         wanted_playerID = arg1
#         await ctx.send(arg1 + '`s playerID is' + wanted_playerID)
#
#     else:
#         await ctx.send("have no permission")


bot.run(TOKEN)
