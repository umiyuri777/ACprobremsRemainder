import discord
from dotenv import load_dotenv
import os
from discord.ext import tasks
from datetime import datetime 
from get_ACproblem import get_ACproblem

load_dotenv()

ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
CHANNEL_ID = int(os.environ['CHANNEL_ID'])

# 接続に必要なオブジェクトを追加
client = discord.Client(intents=discord.Intents.all())

# Botの起動時に動作する処理
@client.event
async def on_ready():
    print('{0.user}にログインしました。'.format(client))
    await client.change_presence(status=discord.Status.online, activity=discord.Game('!observation'))

    loop.start()

@tasks.loop(seconds=30)
async def loop():
    # botが起動するまで待つ
    await client.wait_until_ready()

    # 現在の時刻を取得
    now = datetime.now().strftime('%H:%M')

    # # 現在時刻が9時ならメッセージを送る
    # if now == '09:00':
    problem_url = await get_ACproblem()

    print(problem_url)



    channel = client.get_channel(CHANNEL_ID)
    if channel == None:
        print(f"チャンネルID {CHANNEL_ID} が見つかりませんでした。")
        return 
    messege = '今日の1問\n' + problem_url
    await channel.send(messege)

client.run(ACCESS_TOKEN)