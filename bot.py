#!/usr/bin/python
# -- coding: utf-8 -

import discord
import json
import requests
from discord.ext import commands

TOKEN = '**'

# Префикс комынды боту. В данном случае это '!'
bot = commands.Bot(command_prefix='!')


# Функция test
@bot.command()
async def test(ctx, argu):  # создаем асинхронную фунцию test, читаем аргумент arg
    await ctx.send(argu)  # отправляем обратно аргумент


# Функция hello
@bot.command()
async def hello(ctx):  # Создаём ассинхронную функцию hello
    author = ctx.message.author  # Объявляем переменную author и записываем туда информацию об авторе запроса боту.
    await ctx.send('Hello, {}!'.format(author))  # Отпраляем ответ Hello с обращением к автору.


# Функция отображения случайных картинок rim
@bot.command()
async def rim(ctx, arg_im):  # создаем асинхронную фунцию rim, читаем аргумент arg_im
    response = requests.get('https://some-random-api.ml/img/{}'.format(arg_im))  # Запрос картинки
    json_data = json.loads(response.text)  # Извлекаем JSON

    embed = discord.Embed(color=0x72BAB6, title='Random image with {}'.format(arg_im))  # Создание оформления
    embed.set_image(url=json_data['link'])  # Устанавливаем картинку
    await ctx.send(embed=embed)  # Отправляем


bot.run(TOKEN)  # запускаем бота

