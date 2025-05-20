# tserver.py
import discord
from discord.ext import commands
from discord.ui import View, Button
from tserver.tserver_logic import fetch_recent_testworld_notices

class NoticeButtonView(View):
    def __init__(self, notices):
        super().__init__()
        for idx, (title, url) in enumerate(notices, start=1):
            self.add_item(
                Button(label=f"{idx}. {title}", url=url, style=discord.ButtonStyle.link)
            )

def setup_commands(bot: commands.Bot):
    @bot.command(name="테섭", aliases=["업데이트", "업뎃"])
    async def fetch_testworld_notice(ctx):
        async with ctx.typing():  # ✅ 여기 수정
            notices = fetch_recent_testworld_notices()

        if not notices:
            await ctx.send("⚠️ 공지사항을 불러오는 데 실패했습니다.")
            return

        embed = discord.Embed(
            title="🔍 테스트월드 공지 검색 결과",
            description=f"총 {len(notices)}개의 공지사항이 있습니다.\n클릭 시 [테스트월드 사이트](https://maplestory.nexon.com/Testworld/News/Update)로 이동합니다.",
            color=discord.Color.blurple()
        )

        embed.set_thumbnail(url="https://ssl.nexon.com/s2/game/maplestory/renewal/common/test_world_gmstr_off.png")
        
        embed_text = ""
        for idx, (title, _) in enumerate(notices, start=1):
            embed_text += f"{idx}. {title}\n\n"

        embed.add_field(name="공지 목록", value=embed_text.strip(), inline=False)

        view = NoticeButtonView(notices)
        await ctx.send(embed=embed, view=view)

