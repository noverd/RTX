
import discord

comm = ["!rank"]
import time
from dataranks import r as ranks

TOKEN = 'Nzg4NDQ4NjI3ODk4MDU2NzA2.X9jqAQ.-ULEkwsCHqRJ4bULlAxQ7MYRn2s'

mat = ("сук", 'xуй', "пидр", "бля")


class XCLient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user.name}')
        print(f"ID bot:{self.user.id}")

    async def on_message(self, message):
        global cash
        user_name = str(message.author)
        user = message.author
        ID = user.id
        args = message.content
        chan = message.channel
        guild = message.author.guild
        k = 0
        print("Всё сообщение: " + str(message))
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

        if args.startswith("!rank"):
            kos = 0
            commands_bot = args.split()
            if args.startswith("!rank"):
                for i, s in enumerate(ranks):
                    if s["ID"] == ID and str(s["server_id"]) == str(guild.id) and kos == 0:
                        await chan.send("Ваш ранг равен: " + str(ranks[i]["rank"]))
                        print("ранг найден")
                        kos = 1
                        break
                    else:continue
            elif args.startswith("!buy"):
                print("Команда !buy")
                for i, s in enumerate(ranks):
                    if s["ID"] == ID and s["server_id"] == str(guild.id):
                        print(ranks[i]["rank"])
                        cash = ranks[i]["rank"]
                        print(cash)
                        print(commands_bot)
                if commands_bot in "!buyДоступкгалерее" and cash > 50:
                    print(message.author.guild.ser)
                    role = discord.utils.get(message.server.roles, name="Доступ в Галерею")
                    await client.add_roles(user, role)
                elif commands_bot in "Доступкгалерее" and cash < 50:
                    await chan.send("У вас не достаточно ранга!")
                else:
                    print("error")


        else:
            f = open("dataranks.py", "w")
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
            f.write('# coding: utf8')
            f.write('r = [\n')
            for i in ranks:
                f.write(f'{str(i)},\n')
            f.write(']')
            f.close()
            for s in ranks:
                print(s)

            for x in mat:
                if x in args.lower():
                    await chan.send("не матерись")
                    time.sleep(2)
                    await discord.Guild.ban(guild, user=user, reason="Ты плахая папапо", delete_message_days=1)
                    embed = discord.Embed(color=0xFF7C00,
                                          title="Пользователь " + f"@{user} был забанен на 24 часа.Причана - маты")
                    embed.set_image(
                        url="https://cdn.discordapp.com/attachments/768082564019126292/782184876102254592/489d22e04e9ea5f8.png")
                    await chan.send(embed=embed)
                    time.sleep(86400)
                    embed = discord.Embed(color=0xFF7C00, title="Пользователь " + f"@{user} Разбанен.Возврощайся")
                    embed.set_image(
                        url="https://cdn.discordapp.com/attachments/768082564019126292/782222100780810250/2017-01-06-11-04-1982b2d7e556bdb895daece3edfa0789.jpg")
                    await chan.send(embed=embed)
                    await discord.Guild.unban(guild, user=user, reason="Ты плахая папапо")
                    return


if __name__ == '__main__' or True:
    client = XCLient()
    client.run(TOKEN)
