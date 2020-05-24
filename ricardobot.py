import discord
import random
import json
import datetime

client = discord.Client()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return
#hello
	if message.content.startswith('!hello'):
		await message.channel.send("Hello {}! It's time for some flex".format(message.author.mention))
#pidor
	if message.content.startswith('!pidor'):
		with open('data.json') as infile:
			data = json.load(infile)
		if data['pidor'][1] == str(datetime.date.today()):
			 await message.channel.send("Today's pidor is {}".format(data['pidor'][0]))
			 return	 
		chosen_user = random.choice(client.users)
		if str(chosen_user) not in data['pidors']:
			data['pidors'][str(chosen_user)] = 1
		else:
			data['pidors'][str(chosen_user)] += 1
		data['pidor'] = [str(chosen_user), str(datetime.date.today())]
		await message.channel.send("Pidor of the day is {}! Congratulations!".format(chosen_user.mention))
		await message.channel.send(file=discord.File('media/tenor.gif'))
		with open('data.json', 'w') as outfile:
			json.dump(data, outfile)
#dick
	if message.content.startswith('!dick'):
		with open('data.json') as infile:
			data = json.load(infile)
		if str(message.author) not in data['dicks']:
			data['dicks'][str(message.author)] = [0, 0]

		if data['dicks'][str(message.author)][1] == str(datetime.date.today()):
			 await message.channel.send("You already played today! Come back tomorrow!")
			 return

		value = random.randrange(1, 11)

		if data['dicks'][str(message.author)][0] == 0:
			data['dicks'][str(message.author)][0] += value
			await message.channel.send("Your dick has increased by {}cm".format(value))
		elif data['dicks'][str(message.author)][0] <= 9:
			sign = random.choice([0, 1])
			if not sign:
				value = random.randrange(1, data['dicks'][str(message.author)][0]+1)
				data['dicks'][str(message.author)][0] -= value
				await message.channel.send("Your dick has decreased by {}cm".format(value))
			else:
				data['dicks'][str(message.author)][0] += value
				await message.channel.send("Your dick has increased by {}cm".format(value))
		else:
			sign = random.choice([0, 1])
			if sign:
				data['dicks'][str(message.author)][0] += value
				await message.channel.send("Your dick has increased by {}cm".format(value))
			else:
				data['dicks'][str(message.author)][0] -= value
				await message.channel.send("Your dick has decreased by {}cm".format(value))

		data['dicks'][str(message.author)][1] = str(datetime.date.today())
		with open('data.json', 'w') as outfile:
			json.dump(data, outfile)
#topdick
	if message.content.startswith('!topdick'):
		with open('data.json') as infile:
			data = json.load(infile)
		rating = []
		for user in data["dicks"]:
			rating.append([user, data["dicks"][user][0]])
		rating.sort(key=lambda x: x[1], reverse=True)
		place = 1
		msg = ""
		for user in rating:
			msg += "{}. {} - {}cm\n".format(place, user[0], user[1])
			place += 1
		await message.channel.send("Rating of dicks:\n" + msg)
#toppidors
	if message.content.startswith('!toppidors'):
		with open('data.json') as infile:
			data = json.load(infile)
		rating = []
		for user in data["pidors"]:
			rating.append([user, data["pidors"][user]])
		rating.sort(key=lambda x: x[1], reverse=True)
		place = 1
		msg = ""
		for user in rating:
			msg += "{}. {} - {} times\n".format(place, user[0], user[1])
			place += 1
		await message.channel.send("Top pidors of all time:\n" + msg)
#someone
	if message.content.startswith('!someone'):
		chosen_user = random.choice(client.users)
		await message.channel.send("{}".format(chosen_user.mention))
# Entity
    if message.content.startswith('@Entity'):
		await message.channel.send("-p Дядя Володя")
#song 
	if message.content.startswith("!song"):
		await message.channel.send("Not implemented yet!")
#help 
	if message.content.startswith("!help"):
		await message.channel.send("Not implemented yet!")
#gameslist 
	if message.content.startswith("!games"):
		await message.channel.send("Not implemented yet!")
#tictactoe
	if message.content.startswith("!tictactoe"):
		await message.channel.send("Not implemented yet!")


client.run("NjczOTE3MjY4MTI3NjQ1NzE4.XjrR4g.ix0hw9IXd8pGYt1OfdyTBgE40BQ")
