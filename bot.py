import discord
import random
from search import *
from discord.ext import commands
#from discord import FFmpegPCMAudio




client = commands.Bot(command_prefix=">",help_command=None)

@client.event
async def on_ready():
	print("bot is on ready")

@client.command(pass_context=True)
async def coin_flip(ctx):
	if random.choice([0,1])==1:
		img = 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/d471885e-03de-4b3f-84d7-6a1e3c2ae5db/dejsfkl-23f9e40c-a1f9-4f80-b158-cf3bde383714.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2Q0NzE4ODVlLTAzZGUtNGIzZi04NGQ3LTZhMWUzYzJhZTVkYlwvZGVqc2ZrbC0yM2Y5ZTQwYy1hMWY5LTRmODAtYjE1OC1jZjNiZGUzODM3MTQucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.g8N804eLrck6kvgr7dg2tzkr9C_1pdDXGlJX2UYbh3w'
		title="Coinflip"
		color = 0xFF5733
		desc=f"{ctx.author.mention} Flipped coin, we got **Heads**!"
	else:
		img = 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/d471885e-03de-4b3f-84d7-6a1e3c2ae5db/dejsfkq-9b4bddbd-a548-400a-a05f-c7d4dc1f9c73.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2Q0NzE4ODVlLTAzZGUtNGIzZi04NGQ3LTZhMWUzYzJhZTVkYlwvZGVqc2ZrcS05YjRiZGRiZC1hNTQ4LTQwMGEtYTA1Zi1jN2Q0ZGMxZjljNzMucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.y1UFQTj_7GbzkZ1oU9o-be0yIpBOSEuUZpuW1_l5Sbo'
		title = "Coinflip"
		color = 0xFF5733
		desc = f"{ctx.author.mention} Flipped coin, we got **Tails**!"


	embed = discord.Embed(title=title,
		description=desc)
	embed.set_thumbnail(url=img)
	await ctx.send(embed=embed)

@client.command(pass_context=True)
async def roll_die(ctx):
	result = random.choice([1,2,3,4,5,6])
	title="roll a die"
	color = 0xFF5733
	desc=f"{ctx.author.mention} Rolled a Die, we got **{result}**!"
	if result==1:
		img = 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/d471885e-03de-4b3f-84d7-6a1e3c2ae5db/dejsgml-1232c6d1-cf6c-45c0-82af-a61ffbe35331.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2Q0NzE4ODVlLTAzZGUtNGIzZi04NGQ3LTZhMWUzYzJhZTVkYlwvZGVqc2dtbC0xMjMyYzZkMS1jZjZjLTQ1YzAtODJhZi1hNjFmZmJlMzUzMzEucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.27qF8R_JZuhVAnnBf5p542X2DKJUajFuPccZ1oLq9U8'
	elif result==2:
		img = 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/d471885e-03de-4b3f-84d7-6a1e3c2ae5db/dejsgmh-84c49586-e528-4336-8fd0-56a9ef7b4f99.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2Q0NzE4ODVlLTAzZGUtNGIzZi04NGQ3LTZhMWUzYzJhZTVkYlwvZGVqc2dtaC04NGM0OTU4Ni1lNTI4LTQzMzYtOGZkMC01NmE5ZWY3YjRmOTkucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.pj8Qjplbs_sp4lgURwd0cw5ohFV9nk22vR3Mu5TwSyw'
	elif result==3:
		img = 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/d471885e-03de-4b3f-84d7-6a1e3c2ae5db/dejsgme-47cf8901-fa4f-48eb-a634-1c5751144f76.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2Q0NzE4ODVlLTAzZGUtNGIzZi04NGQ3LTZhMWUzYzJhZTVkYlwvZGVqc2dtZS00N2NmODkwMS1mYTRmLTQ4ZWItYTYzNC0xYzU3NTExNDRmNzYucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.zXf9t1zFYPRhKlufDR3_6UuuH1ibf-yqlIxuSvqyazc'
	elif result==4:
		img = 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/d471885e-03de-4b3f-84d7-6a1e3c2ae5db/dejsgmb-32f7c692-8639-48ee-b759-5f9e0f8777e4.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2Q0NzE4ODVlLTAzZGUtNGIzZi04NGQ3LTZhMWUzYzJhZTVkYlwvZGVqc2dtYi0zMmY3YzY5Mi04NjM5LTQ4ZWUtYjc1OS01ZjllMGY4Nzc3ZTQucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.G5_uBpA6o4m6OPv-XEdzbctb5iSDH5rSm0Fi0fUSpSg'
	elif result==5:
		img = 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/d471885e-03de-4b3f-84d7-6a1e3c2ae5db/dejsgm7-f3f7df1b-989f-476d-baaf-84673d2ab292.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2Q0NzE4ODVlLTAzZGUtNGIzZi04NGQ3LTZhMWUzYzJhZTVkYlwvZGVqc2dtNy1mM2Y3ZGYxYi05ODlmLTQ3NmQtYmFhZi04NDY3M2QyYWIyOTIucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.2o7Qsy253r3KtN5i-CkyHIvFoHjRlejrcmNH5VNnFaU'
	else:
		img = 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/d471885e-03de-4b3f-84d7-6a1e3c2ae5db/dejsgm3-d16d47b1-e1fe-4287-a454-093b1e32e6c2.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2Q0NzE4ODVlLTAzZGUtNGIzZi04NGQ3LTZhMWUzYzJhZTVkYlwvZGVqc2dtMy1kMTZkNDdiMS1lMWZlLTQyODctYTQ1NC0wOTNiMWUzMmU2YzIucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.21bV_80jQug81fLVD-2Haa1isKEYWMlb7fzMt66oXA4'


	embed = discord.Embed(title=title,
		description=desc)
	embed.set_thumbnail(url=img)
	await ctx.send(embed=embed)


@client.command(pass_context=True)
async def help(ctx):
	embed = discord.Embed(title='Help',
		color=discord.Color.blue(),
		description='this is the help for this bot')

	embed.set_author(name="@xXBig_Chungus_69Xx",
		icon_url="https://ih1.redbubble.net/image.982409115.2900/poster,504x498,f8f8f8-pad,600x600,f8f8f8.jpg")


	embed.set_thumbnail(url="https://png.pngtree.com/element_our/png_detail/20181013/code-icon-design-vector-png_125856.jpg")

	embed.add_field(name=">search_anime [name]",
		value="this command will make the bot scrape through the websites kissanimes,gogoanime,9anime and 4anime and returns the result which you can follow along to watch it on thier site",
		inline=False)

	embed.add_field(name=">search_movie [name]",
		value="this command will make the bot scrape through the website soap2day and dramacool and returns the result which you can follow along to watch it on thier site",
		inline=False)

	embed.add_field(name=">flip_coin",
		value="flips a coin and tell wether it was a heads or a tails",
		inline=True)

	embed.add_field(name=">throw_die",
		value="throws a die and tells and tells on what it landed",
		inline=True)

	await ctx.send(embed=embed)

@client.command(pass_context=True)
async def search_anime(ctx,*,anime):
	await ctx.send('please wait')
	results = []
	color = 0xFF5733
	for result in search_kissanime(anime):
		url = result['url']
		title = result['title']
		desc = result['desc']
		img = result['img']

		if title not in results:
			embed=discord.Embed(title=title,
				url=url,
				description=desc,
				color=color)
			embed.set_thumbnail(url=img)
			await ctx.send(embed=embed)

			results.append(title)

	for result in search_gogoanime(anime):
		url = result['url']
		title = result['title']
		desc = result['desc']
		img = result['img']

		if title not in results:
			embed=discord.Embed(title=title,
				url=url,
				description=desc,
				color=color)
			embed.set_thumbnail(url=img)
			await ctx.send(embed=embed)
			results.append(title)

	for result in search_9anime(anime):
		url = result['url']
		title = result['title']
		desc = result['desc']
		img = result['img']

		if title not in results:
			embed=discord.Embed(title=title,
				url=url,
				description=desc,
				color=color)
			embed.set_thumbnail(url=img)
			await ctx.send(embed=embed)
			results.append(title)

	for result in search_4anime(anime):
		url = result['url']
		title = result['title']
		desc = result['desc']
		img = result['img']

		if title not in results:
			embed=discord.Embed(title=title,
				url=url,
				description=desc,
				color=color)
			embed.set_thumbnail(url=img)
			await ctx.send(embed=embed)
			results.append(title)

	if not len(results):
		await ctx.send('no results found :(')

@client.command(pass_context=True)
async def search_movie(ctx,*,movie):
	await ctx.send('please wait')
	results = []
	color = 0xFF5733
	for result in search_soap2day(movie):
		url = result['url']
		title = result['title']
		desc = result['desc']
		img = result['img']

		if title not in results:
			embed=discord.Embed(title=title,
				url=url,
				description=desc,
				color=color)
			embed.set_thumbnail(url=img)
			await ctx.send(embed=embed)
			results.append(title)

	for result in search_dramacool(movie):
		url = result['url']
		title = result['title']
		desc = result['desc']
		img = result['img']

		if title not in results:
			embed=discord.Embed(title=title,
				url=url,
				description=desc,
				color=color)
			embed.set_thumbnail(url=img)
			await ctx.send(embed=embed)
			results.append(title)

	if not len(results):
		await ctx.send('no results found :(')

@client.command(pass_context=True)
async def solve(ctx,*,equation):
	try:
		await ctx.send('calculating......')
		text_soln,img_soln = wolfram_alpha(equation)
		await ctx.send(text_soln)
		await ctx.send(img_soln)
	except:
		await ctx.send('something went wrong :(')





client.run("bot token")