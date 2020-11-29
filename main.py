import discord
import time

mat = ("сук", 'xуй', "пидр", "бля", "го")

ranks = [{"name": "tester100#3585", "rank": 0}, {"name": "gagarinten#5622", "rank": 0}]


class XCLient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user.name}')

    async def on_message(self, message):
        user_name = str(message.author)
        user = message.author
        print(user)
        args = message.content
        chan = message.channel
        guild = message.author.guild
        k = 0
        print(ranks)

        for i, s in enumerate(ranks):
            print(s['name'], ' == ', user_name, s['name'] == user_name)
            if s['name'] == user_name:
                print(s)
                print(ranks[i]['rank'])
                ranks[i]['rank'] += 1
                print(ranks[i]['rank'])
                k = 1
        if k == 0:
            ranks.append({'name': user.name + '#' + user.discriminator, 'rank': 1})

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


client = XCLient()
client.run("Nzc2MDk2NTg4MDQ4MzY3NjQ2.X6v6RQ.tFO5oKzXF6vcJCLvQlGRJRMq9NQ")
