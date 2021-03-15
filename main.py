import discord
import time

from dataranks import rank as ranks



TOKEN = 'Токен Скрыт)'

mat = ("сук", 'xуй', "пидр", "бля", "лядь", "fuck")#Вы можете добавить сюда маты


class XCLient(discord.Client):#Это экземляр класса клиента
    async def on_ready(self):
        print(f'Logged in as {self.user.name}')
        print(f"ID bot:{self.user.id}")

    async def on_message(self, message):#Функиция обробатки сообщений
        user_name = str(message.author)#Определение переменных нужных для работы
        user = message.author
        ID = user.id
        args = message.content
        chan = message.channel
        guild = message.author.guild
        k = 0
        print("Всё сообщение: " + str(message))#Вывод информации о отправителе
        print("Текст сообщения: " + args)
        print("Имя отправителя: " + user_name)
        print("ID отправителя: " + str(ID))
        if bool(user.nick):
            print("Ник отправителя: " + str(user.nick))
        print("Имя отправителя ник? = " + str(bool(user.nick)))
        print("Автор бот? = " + str(user.bot))
        print("Название сервера: " + str(guild.name))
        print("ID сервера: " + str(guild.id))
        print("Количество членов сервера:" + str(guild.member_count))
        print(ranks)

        if args.startswith("!rank"): #Определение команд
            for i, s in enumerate(ranks):
                if s["ID"] == ID and str(s["server_id"]) == str(guild.id):
                    await chan.send(f"{user.mention} твой ранг - {str(ranks[i]['rank'])}")
                    break
                else:
                    print("error")

        else:
            f = open("dataranks.py", "w")#Чтение и запись в файл dataranks.py
            f.close()
            for i, s in enumerate(ranks):
                print(s['ID'], ' == ', ID, s['ID'] == ID)
                if s["ID"] == ID and s["server_id"] == str(guild.id) and not args.startswith("!"):
                    print(s)
                    print(ranks[i]['rank'])
                    ranks[i]['rank'] += 1
                    print(ranks[i]['rank'])
                    k = 1
            if k == 0:
                ranks.append(
                    {"ID": ID, 'name': user_name, 'rank': 1, "server_name": str(guild.name),
                     "server_id": str(guild.id), "member_count": str(guild.member_count)})
            f = open("dataranks.py", "r+")
            f.write('r = [\n')
            for i in ranks:
                f.write(f'{str(i)},\n')
            f.write(']')
            f.close()
            for s in ranks:
                print(s)

            for x in mat:#определение матов
                if x in args.lower():
                    await chan.send(f'{user.mention} не матерись!')
                    time.sleep(2)
                    await discord.Guild.ban(guild, user=user, reason="Нецензурная лексика", delete_message_days=1)
                    embed = discord.Embed(color=0xFF7C00,
                                          title=f"Пользователь {user.mention} был забанен на 24 часа. Причана - маты")
                    embed.set_image(
                        url="https://cdn.discordapp.com/attachments/768082564019126292/782184876102254592/489d22e04e9ea5f8.png")
                    await chan.send(embed=embed)
                    print(f'Забанен {user}')
                    time.sleep(86400)
                    embed = discord.Embed(color=0xFF7C00, title=f"Пользователь {user.mention} разбанен. Возврощайся")
                    embed.set_image(
                        url="https://cdn.discordapp.com/attachments/768082564019126292/782222100780810250/2017-01-06-11-04-1982b2d7e556bdb895daece3edfa0789.jpg")
                    await chan.send(embed=embed)
                    await discord.Guild.unban(guild, user=user, reason="Прошел срок")
                    print(f'Разбанен {user}')
                    return


if __name__ == '__main__' or True:#СпиДRun
    client = XCLient()
    client.run(TOKEN)
