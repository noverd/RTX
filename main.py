import discord
from random import randint, choice
from dataranks import r as ranks
from server_setting import sc as server_cfg
import datetime, time

deflaut_permission_shop = "ADMINISTRATOR"
deflaut_prefix = "!"
deflaut_prefix_permission = "ADMINISTRATOR"
buy_item = ["Доступ к галерее"]
buy_list = ["!buy Доступ к галерее"]
buy_cash = ["1000"]
buy_descriptor = ["Роль для доступа в галерею"]
TOKEN = 'ODQxNjYxMjM4NDM2OTU0MTMy.YJqAHA.aMM2L6MtEmEVZgy8QFnhgzED8Cw'
works = ["Вы продали себя в рабство на 30 лет.", "Вы устроились тестировщиком лекарств. У вас теперь 3 руки",
         "Вы стали горничной и работали 95. Но за это время инфляция...",
         "Вы ушли в армию.Вы заработали там 5.900.156 :dollar: .  Но расходы на лечение..."]
mat = ("сук", 'xуй', "пидр", "бля")


def permission(per, role):
    if role == "ADMINISTRATOR":
        return per.administrator()
    elif role == "INVITE":
        return per.create_instant_invite()
    elif role == "KICK":
        return per.kick_members()
    elif role == "BAN":
        return per.ban_members()
    elif role == "MANAGE_CHANNEL":
        return per.manage_channels()
    elif role == "MANAGE_GUILD":
        return per.manage_guild()
    elif role == "REACTION":
        return per.add_reactions()
    elif role == "GUILD":
        return per.manage_guild()
    elif role == "AUDIT_LOG":
        return per.view_audit_log()
    elif role == "SUPER_SPEAKER":
        return per.priority_speaker()
    elif role == "STREAM":
        return per.stream()
    elif role == "READ_MESSAGE":
        return per.read_message()
    elif role == "VIEW_CHANNEL":
        return per.view_channel()
    elif role == "SEND_MESSAGE":
        return per.send_messages()
    elif role == "SEND_TTS_MESSAGE":
        return per.send_tts_messages()
    elif role == "MODERATION":
        return per.manage_messages()
    elif role == "EMBED":
        return per.embed_links()
    elif role == "SEND_FILE":
        return per.attach_files()
    elif role == "READ_HISTORY_MESSAGE":
        return per.read_message_history()
    elif role == "PING_EVERYONE":
        return per.mention_everyone()
    elif role == "EXTERNAL_EMOJI":
        return per.external_emojis()
    elif role == "USE_EXTERNAL_EMOJI":
        return per.use_external_emojis()
    elif role == "VIEW_INTEGRATION":
        return per.view_guild_insights()
    elif role == "CONNECT":
        return per.connect()
    elif role == "SPEAK":
        return per.speak()
    elif role == "MUTE_VOICE":
        return per.mute_members()
    elif role == "DEAFEN":
        return per.deafen_members()
    elif role == "MOVE_VOICE":
        return per.move_members()
    elif role == "VOICE_ACTIVATE":
        return per.use_voice_activation()
    elif role == "CHANGE_NICK":
        return per.change_nickname()
    elif role == "MANAGE_ROLE":
        return per.manage_roles()
    elif role == "MANAGE_PERMISSION":
        return per.manage_permissions()
    elif role == "MANAGE_WEBHOOK":
        return per.manage_webhooks()
    elif role == "USE_SLASH_COMMAND":
        return per.use_slash_commands()
    elif role == "REQUEST_TO_SPEAK":
        return per.request_to_speak()


class XCLient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user.name}')
        print(f"ID bot:{self.user.id}")

    async def on_message(self, message):
        global cash, buy_item, prefix, prefix_permission, nomer
        user_name = str(message.author)
        user = message.author
        ID = user.id
        args = message.content
        chan = message.channel
        guild = message.author.guild
        k = 0
        kost = True
        for i, s in enumerate(server_cfg):
            if s["id"] == guild.id:
                nomer = i
                prefix = s["prefix"]
                add_to_shop = s["permission_shop"]
                prefix_permission = s["permission_set_prefix"]
                kost = False
        if kost:
            server_cfg.append({"id": guild.id, "name": guild.name, "prefix": deflaut_prefix,
                               "permission_shop": deflaut_permission_shop,
                               "permission_set_prefix": deflaut_prefix_permission})
            prefix = deflaut_prefix
            add_to_shop = deflaut_permission_shop
            prefix_permission = deflaut_prefix_permission

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

        if args.startswith(prefix):
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
                                              description=f"Вот что вы можете купить:\n{buy_item_list}", color=0x0beb10)
                        await chan.send(embed=liste)
            elif body == "work":
                work = randint(10, 50)
                for i, s in enumerate(ranks):
                    print(f"si{s}")
                    if s["ID"] == ID and s["server_id"] == str(guild.id):
                        ranks[i]["cash"] += work
                worke = discord.Embed(title=":dollar: Работа :dollar:", color=0x0beb10,
                                      description=f"{choice(works)}\nВы заработали {work} :dollar: \n Вы можете узнать свой баланс - `!balance`\n Первести деньги(Не реализованно) - `!give`\nКупить что-то - `!buy`(Посмотреть что купить - `!buy list`)")
                await chan.send(embed=worke)
            elif body == "balance":
                for i, s in enumerate(ranks):
                    if s["ID"] == ID and s["server_id"] == str(guild.id):
                        balance = discord.Embed(title=":dollar: Твой баланс :dollar:",
                                                description=f"Твой баланс: {ranks[i]['cash']} :dollar:\nЗаработать деньги - `{prefix}work`\n Первести деньги(Не реализованно) - `{prefix}give`\nКупить что-то - `{prefix}buy`(Посмотреть что купить - `!buy list`)",
                                                color=0x0beb10)
                        await chan.send(embed=balance)
            elif body == "set_prefix" and permission(guild.guild_permissions, prefix_permission):
                server_cfg[nomer]["prefix"] = arg[0]
                embed = discord.Embed(title="Префик",
                                      description=f"Префикс успешно установлен!\n`{prefix}buy_add` - Добавить вещь в `{prefix}buy list`",
                                      color=0x0beb10)

                await chan.send(embed=embed)
            elif body == "set_permisson":
                if arg[0] == "prefix":
                    server_cfg[nomer]["permission_set_prefix"] = arg[1]
                elif arg[0] == "shop":
                    server_cfg[nomer]["permission_shop"] = arg[1]



        else:
            for i, s in enumerate(server_cfg):
                if s["id"] == ID and s["server_id"] == str(guild.id) and not args.startswith("!"):
                    k = 1
            if k == 0:
                ranks.append(
                    {"ID": ID, 'name': user_name, "server_name": str(guild.name),
                     "server_id": str(guild.id), "member_count": str(guild.member_count), "cash": 0})
            f = open("dataranks.py", "r+")
            f.write('# coding: utf8\n')
            f.write('r = [\n')
            for i in ranks:
                f.write(f'{str(i)},\n')
            f.write(']')
            f.close()
            for s in ranks:
                print(s)
            for i, s in enumerate(ranks):
                print(s['ID'], ' == ', ID, s['ID'] == ID)
                if s["ID"] == ID and s["server_id"] == str(guild.id) and not args.startswith("!"):
                    k = 1
            if k == 0:
                ranks.append(
                    {"ID": ID, 'name': user_name, "server_name": str(guild.name),
                     "server_id": str(guild.id), "member_count": str(guild.member_count), "cash": 0})
            f = open("server_setting.py", "r+")
            f.write('# coding: utf8\n')
            f.write('sc = [\n')
            for i in server_cfg:
                f.write(f'{str(i)},\n')
            f.write(']')
            f.close()
            for s in server_cfg:
                print(s)


if __name__ == '__main__' or True:
    client = XCLient()
    client.run(TOKEN)
