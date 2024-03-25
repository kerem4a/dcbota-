import discord
import random
import requests
from discord.ext import commands
from model12 import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def carp (ctx, sayi1=0 , sayi2=0):
    carpim = sayi1 * sayi2
    await ctx.send(carpim)

@bot.command()
async def bol (ctx, sayi1=0 , sayi2=0):
    bolme = sayi1 / sayi2
    await ctx.send(bolme)

@bot.command()
async def top (ctx, sayi1=0 , sayi2=0):
    toplama = sayi1 + sayi2
    await ctx.send(toplama)

@bot.command()
async def cık (ctx, sayi1=0 , sayi2=0):
    cıkarma = sayi1 - sayi2
    await ctx.send(cıkarma)

@bot.command()
async def yazitura(ctx):
    yanlar = ['Yazı', 'Tura']
    sonuc = random.choice(yanlar)
    await ctx.send(f'Sonuç: {sonuc}')  

@bot.command()
async def zar(ctx):
    sayi = random.randint(1, 6)
    await ctx.send(f'Zar attın ve {sayi} geldi!')

@bot.command()
async def hava_durumu(ctx, *, sehir: str):
    api_key = "ff4d0f71153fc14f03f0ef1410af08a9 " 
    url = f'http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    durum = data['weather'][0]['description']
    sicaklik = data['main']['temp']
    await ctx.send(f'{sehir} hava durumu: {durum}, Sıcaklık: {sicaklik}°C')

@bot.command()
async def emoji(ctx, tur: str):
    if tur.lower() == 'hayvanlar':
        emojis = ['🐱', '🐶', '🐰', '🦊', '🐼', '🐍', '🐢', '🐬', '🦄', '🦜', '🐘', '🦒', '🦏', '🐅',
              '🐆', '🐎', '🐖', '🐕', '🦔', '🦓', '🐀', '🦎', '🐿️', '🐾']
    elif tur.lower() == 'yiyecekler':
        emojis = ['🍎', '🍕', '🍔', '🍟', '🍦', '🍓', '🍫', '🍰', '🍩', '🌮', '🥗', '🍜', '🍣', '🥞','🍇',
                  '🥑', '🥪', '🍒', '🍔', '🥙', '🍕', '🌭', '🥨', '🍳', '🍤', '🥓', '🧀']
    elif tur.lower() == 'yuz-ifadeleri':
        emojis = ['😄', '😊', '😎', '😢', '😡', '😍', '😋', '😐', '😇', '🥺', '😷', '😲', '😰', '😰',
              '😑', '😞', '😠', '🙄', '😳', '😭', '😴', '😩', '😲', '😁', '🤣', '😂', '😅']
    else:
        await ctx.send('Geçersiz emoji türü. Lütfen hayvanlar, yiyecekler veya yuz-ifadeleri girin.')
        return

    emoji = random.choice(emojis)
    await ctx.send(emoji)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *liste: str):
    """Chooses between multiple choices good luck."""
    await ctx.send(random.choice(liste))    

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))




bot.run("")
