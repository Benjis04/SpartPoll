import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '+', description = '')


@bot.event
async def on_ready():
	print('Pret !\n')
        activity = discord.Game(name="SPARTACUBE.fr", type=3)
        await bot.change_presence(status=discord.Status.idle, activity=activity)
        print("-----------")

@bot.event
async def on_message(message):
	#Un message a été détecté
	print("\nMessage de", message.author, "dans", message.channel, "qui contient '", message.content, "'")
	
	#Fonction pour tester si le message est bien dans le salon approprié (ex : suggestion). Si oui la fonction retourne 1 sinon 0.
	def check(message):
		messageChannel = message.channel
		return str(messageChannel) == 'NOM DU SALON POUR LES REACTIONS' #or str(messageChannel) == <Autre channel du serveur à ajouter des réactions>
	
	#Phase de test grace à la fonction check crée aupparavant
	test = check(message)
	if test == 1:
		print(test, "; Bon Channel --> Le bot a ajouté les réactions\n")
		print("-----------")
		await message.add_reaction("✅")
		await message.add_reaction("❌")
	else:
		print(test, "; Mauvais channel --> Le bot n'a pas ajouté les réactions\n")
		print("-----------")
		return

		
bot.run('VOTRE TOKEN ICI')
