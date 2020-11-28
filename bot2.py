#!/usr/bin/python
# -- coding: utf-8 -
import discord

TOKEN = '**'
XX = ('aa', 'bb', 'cc')  # Список слов на которые реагирует наш бот


class MyClient(discord.Client):
    # Функция реакции на старт бота
    async def on_ready(self):
        print(f'Logged in as {self.user.name}')

    # Функция реакции на сообщения
    async def on_message(self, message):

        # Исключаем реакцию бота на самого себя
        if message.author.id == self.user.id:
            return

        # Реакция на команду !hello
        if message.content.startswith('!hello'):
            await message.channel.send(f'Hello {message.author.mention}')

        # Логика реакции бота
        for i in XX:
            if i in message.content:
                await message.channel.send(f'{message.author.mention}, не надо так\nx{c}')
                return


client = MyClient()
client.run(TOKEN)
