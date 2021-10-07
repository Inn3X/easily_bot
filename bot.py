import discord
from discord.ext import commands

class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged on as {0}!' .format(self.user))
	async def on_message(self,message):
		print('Message from {0.author}: {0.content}' .format(message))
bot = MyClient()
bot = commands.Bot(command_prefix='!')
@bot.event
async def on_message_edit(before,after): #изменение текста
    channel = bot.get_channel(894939865026805801)
    if before.content == after.content:
        return
    await channel.send(f" **Старое сообщение**:`\n{before.content}`\n**Новое сообщение**:\n`{after.content}`")

@bot.command(pass_context = True) #Вызываем проверку текста
@commands.has_permissions( administrator = True)
async def ban(ctx,member: discord.Member,*,reason = None): #сама команда в нашем случае "ban"
    embed = discord.Embed(title = 'Ban',colour = discord.Color.red())
    await ctx.channel.purge( limit = 1 )
    await member.ban(reason = reason)
    embed.set_author(name = member.name,icon_url = member.avatar_url)
    embed.add_field(name ='Ban user', value = 'Banned user : {}'.format (member.mention))
    embed.set_footer(text = 'Был забанен администратором {}'.format(ctx.author.name), icon_url = ctx.author.avatar_url )
    await ctx.send(embed = embed)
@bot.command(pass_context = True) #Вызываем проверку текста
async def команды(ctx,*args):
    Comds = ("**тут ничего нет**") #сама команда в нашем случае "команды"
    embed = discord.Embed(title = 'Команды:',colour = discord.Color.teal())
    embed.add_field(name = 'Префикс:"!"' , value= Comds)
    await ctx.send(embed = embed)
#@bot.command(pass_context = True)
bot.run(process.env.BOT_TOKEN)
