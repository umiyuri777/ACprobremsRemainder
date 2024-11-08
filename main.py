import discord
from dotenv import load_dotenv
import os
from discord.ext import tasks
from datetime import datetime 
from get_ACproblem import get_ACproblem

load_dotenv()

ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
CHANNEL_ID = os.environ['CHANNEL_ID']

# 接続に必要なオブジェクトを追加
client = discord.Client()

@tasks.loop(seconds=30)
async def loop():
    # botが起動するまで待つ
    await client.wait_until_ready()

    # 現在の時刻を取得
    now = datetime.now().strftime('%H:%M')

    # 現在時刻が9時ならメッセージを送る
    if now == '09:00':
        problem_url = get_ACproblem()

        channel = client.get_channel(CHANNEL_ID)
        await channel.send('今日の1問\n', problem_url)

loop.start()
client.run(ACCESS_TOKEN)