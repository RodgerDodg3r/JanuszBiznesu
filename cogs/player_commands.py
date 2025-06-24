import discord
import random
import math
from discord.ext import commands

from functions.guild_functions import guild_get_data
from functions.player_functions import *


class PlayerCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="profit")
    async def command_player_get_profit(self, ctx):
        player_update_config(ctx.author.id)

        guild_data = guild_get_data()
        if guild_data["bot_channel"] != ctx.message.channel.id:
            await ctx.message.delete()
            await ctx.author.send(
                f"❌ | Nie możesz używać {ctx.message.channel.mention} do używania komend Janusza Biznesu"
            )
            return

        player_data = player_get_data(ctx.author.id)
        last_update = player_data["last_update"]
        now = time.time()

        print(now - last_update)
        # ⏳ Too soon to claim
        if now - last_update < 3600:
            cooldown_messages = [
                "⏳ | Spokojnie, Januszu. Wypłata jeszcze nie gotowa. Idź na fajka i wróć później.",
                "❌ | Ty to byś chciał kasę co 5 minut? To nie ZUS po piątku – wróć później!",
                "⏳ | Szef mówi, że jak jeszcze raz zapytasz o wypłatę, to sam sobie ją możesz wydrukować.", 
                "💤 | Wypłata śpi. Ty też się położ, wróć za chwilę.", 
                "🚫 | Musisz poczekać. Nawet złodzieje mają lepszy timing niż ty.", 
                "❌ | Jeszcze nie teraz! Pracuj dłużej, narzekaj więcej, a może coś skapnie.", 
            ]
            await ctx.message.reply(random.choice(cooldown_messages))
            return 

        # ✅ Time to claim profit
        payout_messages = [
            "💸 | Wypłata wpadła! Nie wydaj wszystkiego od razu na kebsa i energetyki.",
            "✅ | Kasa się zgadza! Szef chciał dać mniej, ale przypomniałeś mu o umowie... słownej.",
            "🤑 | Wypłata poszła na konto. No, chyba że komornik był szybszy.",
            "💼 | Przelew dotarł. Czas na świętowanie – bieda wersja: chleb z keczupem.",
            "💰 | Zrobiłeś swoje, hajs się zgadza. A teraz szybko do Żabki, zanim wszystko przepadnie!",
            "📥 | Wypłata odebrana! Czujesz się bogaty, dopóki nie spojrzysz na ceny w Biedronce.",
            "🪙 | Kilka złociszy wpadło. Nie pytaj za co, po prostu się ciesz.",
        ]

        profit_per_hour = player_get_profit(ctx.author.id)
        hours_passed = math.floor((now - last_update) / 3600)
        total_earned = profit_per_hour * hours_passed

        # 💰 Update data
        player_data["money"] += total_earned
        player_data["last_update"] = now
        player_save_data(ctx.author.id, player_data)

        currency = guild_data["currency"]
        await ctx.message.reply(
            f"{random.choice(payout_messages)}\n+{int(total_earned)} {currency} 💵"
        )


    @commands.command(name="pracuj")
    async def command_player_working(self, ctx):

        player_update_config(ctx.author.id)

        guild_data = guild_get_data()
        if (guild_data["bot_channel"] != ctx.message.channel.id):
            await ctx.message.delete()
            await ctx.author.send(f"❌ | Nie możesz używać {ctx.message.channel.mention} do używania komend Janusza Biznesu")
            return

        profit = random.randint(10, 50)
        player_data = player_get_data(ctx.author.id)
        player_data["money"] = player_data["money"] + profit

        player_save_data(ctx.author.id,player_data)
        
        guild_data = guild_get_data()
        currency = guild_data["currency"]

        messages = [
            f"💼 Zasuwałeś jak dzik w kukurydzy – profit w kieszeni i zapach potu w gratisie.",
            "🛠️ Zrobiłeś czarną robotę za kogoś innego. Jak zawsze, zapłacili jak za zboże – czyli gówno.",
            "🧻 Sprzątałeś po imprezie swingersów. Zarobione, ale twoja dusza potrzebuje prysznica.",
            "🪵 Rąbałeś drewno jak ojciec po trzech piwach – krzywo, ale skutecznie. Hajs się zgadza.",
            "🚽 Odblokowałeś kibelek w Solarium Shalom. Znalazłeś i straciłeś resztki godności.",
            "📦 Przenosiłeś kartony z 'Czeskiej mety'. Niby praca, ale teraz masz haluny od oparów.",
            "🎪 Dorabiałeś w wędrownym cyrku jako człowiek-pomidor. Ktoś cię opluł, ktoś zapłacił – życie.",
            "🥴 Pracowałeś pod stołem. I to dosłownie. Pracodawca był dziwny, ale zapłacił gotówką.",
            "💃 Zatańczyłeś na stole w klubie za piątaka i tipsa. Bieda, ale honor jeszcze jako-tako.",
            "🍺 Dobiłeś 8 godzin w sklepie Ropucha. Zarobiłeś więcej niż wydałeś na browary – sukces!",            
        ]

        await ctx.message.reply(f"{random.choice(messages)}\n + {profit} {currency} 💵")



    @commands.command(name="panel")
    async def command_player_panel(self, ctx):

        player_update_config(ctx.author.id)

        guild_data = guild_get_data()
        if (guild_data["bot_channel"] != ctx.message.channel.id):
            await ctx.message.delete()
            await ctx.author.send(f"❌ | Nie możesz używać {ctx.message.channel.mention} do używania komend Janusza Biznesu")
            return

        guild_currency = guild_data["currency"]

        player_data = player_get_data(ctx.author.id)
        player_money = player_data["money"]

        player_money_per_hour = player_get_profit(ctx.author.id)

        embed = discord.Embed(color=0xcf25be)
        
        embed.add_field(name=f"{guild_currency}  💵", value=f"{player_money}", inline=True)
        embed.add_field(name=f"{guild_currency}/h  🕛", value = f"{player_money_per_hour}\n\n", inline=True)

        for building in player_data["buildings"]:
            building_quantity = player_data["buildings"][building]["quantity"]
            bulding_description = player_data["buildings"][building]["description"]
            profit_per_h = player_data["buildings"][building]["per_h"] * building_quantity
            cost = player_data["buildings"][building]["cost"]

            embed.add_field(name = f"{building}", value = f"**Ilość**: `{building_quantity}`\n**Profit/h**: `{profit_per_h} 💵`\n**Koszt**: {cost} {guild_currency}\n**Opis**: `{bulding_description}`", inline = False)
    
        embed.set_footer(text="Janusz Biznesu made by RogerDodg3r")
        embed.set_author(name="Panel twojego finansowego imperium", icon_url= ctx.author.avatar.url)


        await ctx.send(embed=embed)

    




async def setup(bot):
    await bot.add_cog(PlayerCommands(bot))





