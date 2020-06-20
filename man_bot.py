import discord
from dico import dico
from cle import cle

from discord.ext import commands

#création du bot
bot = commands.Bot(command_prefix='$')
lst_bot_admin = ['cleanchat']
admin = ['260030193937154048','270590616029757451']

#détecter quand le bot est prêt
@bot.event
async def on_ready():
    print("Bot allumé")
    await bot.change_presence(status=discord.Status.online,activity=discord.Game("Prêt à aider"))

#créer la commande $man
@bot.command()
async def Man_py(ctx):
    await ctx.send(dico['man'])

@bot.command()
async def man(ctx, arg):
    if arg in lst_bot_admin and not str(ctx.message.author.id) in admin:
        await ctx.send("Tu as ni la permission ni l'utilitée d'utiliser ce bot")
    else:
        await ctx.send(dico[arg.lower()])

#clé du bot

bot.run(str(cle))