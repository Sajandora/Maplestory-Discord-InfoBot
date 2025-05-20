import discord
from discord.ext import commands
import asyncio
import sys
from azmoth.azmoth import setup_commands as setup_azmoth
from scouter.scouter import setup_commands as setup_scouter
from tserver.tserver import setup_commands as setup_tserver
from dotenv import load_dotenv 
import os  

# 디스코드 봇 토큰
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Windows 환경 대응
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# 인텐트 설정
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user}')

# 명령어 등록
setup_azmoth(bot)
setup_scouter(bot)
setup_tserver(bot)

# 봇 실행
if TOKEN:
    bot.run(TOKEN)
else:
    print("❌ DISCORD_BOT_TOKEN 환경 변수가 설정되지 않았습니다.")
