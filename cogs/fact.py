from random import choice
import discord, os, sys, platform, aiohttp, json
from discord.ext import commands
from Resources import factre as ft
import re
import random
bot_channel = 'bot-chat'

if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config

class fact(commands.Cog, name="fact"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="givefact", aliases=['Fact', 'FACT', 'FAct', 'FaCt', 'FACt', 'facT'])
    async def fact(self, message, fact_type="None"):
        channels = ['bot-chat']
        if message.channel.name in channels:  # bot only run command in joke-only channel
            if fact_type == "None":
                fact = ft.get_fact()  # return random fact
                embed = discord.Embed(description=fact, colour=0x00ff00)
            elif fact_type.upper() == 'NUMBER':
                n_fact = ft.get_random_number_fact()  # return random number fact
                embed = discord.Embed(description=n_fact, colour=0x00ff00)
            elif fact_type.isdigit():
                n_fact = ft.get_number_fact(fact_type)  # return number fact
                embed = discord.Embed(description=n_fact, colour=0x00ff00)
            elif re.match(r'\d{2}/\d{2}', fact_type):
                n_fact = ft.get_date_fact(fact_type)  # return date fact
                embed = discord.Embed(description=n_fact, colour=0x00ff00)
            elif fact_type.upper() == 'ANIMAL':  # return random animals fact
                animals_fact = ft.get_animals_fact()
                embed = discord.Embed(description=animals_fact, colour=0x00ff00)
            elif fact_type.upper() == 'DOG':  # return dog fact
                animals_fact = ft.animal_fact(fact_type)
                embed = discord.Embed(description=animals_fact, colour=0x00ff00)
            elif fact_type.upper() == 'CAT':  # return cat fact
                animals_fact = ft.animal_fact(fact_type)
                embed = discord.Embed(description=animals_fact, colour=0x00ff00)
            elif fact_type.upper() == 'PANDA':  # return panda fact
                animals_fact = ft.animal_fact(fact_type)
                embed = discord.Embed(description=animals_fact, colour=0x00ff00)
            elif fact_type.upper() == 'FOX':  # return fox fact
                animals_fact = ft.animal_fact(fact_type)
                embed = discord.Embed(description=animals_fact, colour=0x00ff00)
            elif fact_type.upper() == 'BIRD':  # return bird fact
                animals_fact = ft.animal_fact(fact_type)
                embed = discord.Embed(description=animals_fact, colour=0x00ff00)
            elif fact_type.upper() == 'KOALA':  # return koala fact
                animals_fact = ft.animal_fact(fact_type)
                embed = discord.Embed(description=animals_fact, colour=0x00ff00)
            else:
                embed = discord.Embed(
                    title='Invalid Input',
                    description='Please try command "cyb!help" for more information',
                    colour=0xff0000)
                gif_list =['https://media.giphy.com/media/TqiwHbFBaZ4ti/giphy.gif',
                            'https://media.giphy.com/media/3osxY9kuM2NGUfvThe/giphy.gif',
                            'https://media.giphy.com/media/YyKPbc5OOTSQE/giphy.gif',
                            'https://media.giphy.com/media/li0dswKqIZNpm/giphy.gif',
                            'https://media0.giphy.com/media/ljtfkyTD3PIUZaKWRi/giphy.gif',
                            'https://media.giphy.com/media/HNEmXQz7A0lDq/giphy.gif',
                            'https://media.giphy.com/media/4au7PZFkWSjnIsnZXL/giphy.gif',
                            'https://media1.giphy.com/media/3Z1oSJQpkDZBvJVsUT/giphy.gif',
                            'https://media.giphy.com/media/vKz8r5aTUFFJu/giphy.gif',
                            'https://media.giphy.com/media/kEtm4mSTbxvH7j3uCu/giphy.gif',
                            'https://media.giphy.com/media/bi6RQ5x3tqoSI/giphy.gif']

                embed.set_image(url = random.choice(gif_list))

            await message.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(fact(bot))