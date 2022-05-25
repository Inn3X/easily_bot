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
async def on_message_edit(before,after): #event when message edit
    channel = bot.get_channel('logs channel here')
    if before.content == after.content:
        return
    await channel.send(f" **Old message**:`\n{before.content}`\n**New message**:\n`{after.content}`")

@bot.command(pass_context = True) #checking what u wrote, if it's 'ban' then bot will be work on this command
@commands.has_permissions( administrator = True)
async def ban(ctx,member: discord.Member,*,reason = None): #command "ban"
    embed = discord.Embed(title = 'Ban',colour = discord.Color.red())
    await ctx.channel.purge( limit = 1 )
    await member.ban(reason = reason)
    embed.set_author(name = member.name,icon_url = member.avatar_url)
    embed.add_field(name ='Ban user', value = 'Banned user : {}'.format (member.mention))
    embed.set_footer(text = 'Was banned by: {}'.format(ctx.author.name), icon_url = ctx.author.avatar_url )
    await ctx.send(embed = embed)
@bot.command(pass_context = True) #Also checking command
async def commands(ctx,*args):
    Comds = ("**there's no here**") #command "commands"
    embed = discord.Embed(title = 'Commands:',colour = discord.Color.teal())
    embed.add_field(name = 'Prefix:"!"' , value= Comds)
    await ctx.send(embed = embed)
#@bot.command(pass_context = True)
bot.run(process.env.BOT_TOKEN)
