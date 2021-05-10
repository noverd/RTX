import discord
from random import randint, choice
from dataranks import r as ranks
import datetime
buy_item = ["Доступ к галерее"]
buy_list = ["!buy Доступ к галерее"]
buy_cash = ["1000"]
buy_descriptor = ["Роль для доступа в галерею"]
TOKEN = 'Nzg4NDQ4NjI3ODk4MDU2NzA2.X9jqAQ.-LDCes1S2ex0yInnWWj0D_5sBvs'
works = ["Вы продали себя в рабство на 30 лет.", "Вы устроились тестировщиком лекарств. У вас теперь 3 руки",
         "Вы стали горничной и работали 95. Но за это время инфляция...",
         "Вы ушли в армию.Вы заработали там 5.900.156 :dollar: .  Но расходы на лечение..."]
mat = ("сук", 'xуй', "пидр", "бля")


class XCLient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user.name}')
        print(f"ID bot:{self.user.id}")

    async def on_message(self, message):
        global cash, buy_item
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

        if args.startswith("!"):
            kos = 0
            body = args.split("!")[1].split()[0]
            arg = args.split("!")[1].split()
            print(f"Тело команды: {body}")
            print(f"Аргменты {arg}")
            del arg[0]
            if body == "buy":
                buy_arg = arg[0]
                for i, x in enumerate(arg):
                    print()
                    if i == 0:
                        print("cont")
                        continue
                    buy_arg = buy_arg + " " + x
                    print("add")
                print(buy_arg)
                print("Команда !buy")
                for i, s in enumerate(ranks):
                    if s["ID"] == ID and s["server_id"] == str(guild.id):
                        cash = int(ranks[i]["cash"])
                        print(cash)
                if buy_arg == "Доступ к галерее" and cash > 9999:
                    print(message.author.guild.name)
                    role = discord.utils.get(message.guild.roles, name="Доступ в Галерею")
                    await user.add_roles(role)
                elif buy_arg == "Доступ к галерее" and cash < 10000:
                    await chan.send("У вас не достаточно денег")
                else:
                    if buy_arg == "list":
                        buy_item_list = ""
                        for i, x in enumerate(buy_item):
                            buy_item_list = buy_item_list + "`" + buy_item[i] + "` - " + buy_descriptor[
                                i] + ". Цена - " + buy_cash[i] + " :dollar:\n"
                        print(buy_item_list)
                        liste = discord.Embed(title="Список вещей для покупки",
                                              description=f"Вот что вы можете купить:\n{buy_item_list}",color=0x0beb10)
                        await chan.send(embed=liste)
            elif body == "work":
                work = randint(10, 50)
                for i, s in enumerate(ranks):
                    if s["ID"] == ID and s["server_id"] == str(guild.id):
                        ranks[i]["cash"] += work
                worke = discord.Embed(title=":dollar: Работа :dollar:", color=0x0beb10,
                                      description=f"{choice(works)}\nВы заработали {work} :dollar: \n Вы можете узнать свой баланс - `!balance`\n Первести деньги(Не реализованно) - `!give`\nКупить что-то - `!buy`(Посмотреть что купить - `!buy list`)")
                await chan.send(embed=worke)
            elif body == "balance":
                for i, s in enumerate(ranks):
                    if s["ID"] == ID and s["server_id"] == str(guild.id):
                        balance = discord.Embed(title=":dollar: Твой баланс :dollar:",
                                                description=f"Твой баланс: {ranks[i]['cash']} :dollar:\nЗаработать деньги - `!work`\n Первести деньги(Не реализованно) - `!give`\nКупить что-то - `!buy`(Посмотреть что купить - `!buy list`)",
                                                color=0x0beb10)
                        await chan.send(embed=balance)



        else:
            for i, s in enumerate(ranks):
                print(s['ID'], ' == ', ID, s['ID'] == ID)
                if s["ID"] == ID and s["server_id"] == str(guild.id) and not args.startswith("!"):
                    k = 1
            if k == 0:
                ranks.append(
                    {"ID": ID, 'name': user_name, "server_name": str(guild.name),
                     "server_id": str(guild.id), "member_count": str(guild.member_count), cash: 0})
            f = open("dataranks.py", "r+")
            f.write('# coding: utf8\n')
            f.write('r = [\n')
            for i in ranks:
                f.write(f'{str(i)},\n')
            f.write(']')
            f.close()
            for s in ranks:
                print(s)


if __name__ == '__main__' or True:
    client = XCLient()
    client.run(TOKEN)
