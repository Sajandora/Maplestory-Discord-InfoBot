import discord
import urllib.parse

class ScouterView(discord.ui.View):
    def __init__(self, url: str):
        super().__init__()
        self.add_item(discord.ui.Button(label="🔗 사이트 바로가기", url=url))

def create_scouter_embed_with_button(nickname: str = None):
    base_url = "https://maplescouter.com"

    if nickname:
        encoded_name = urllib.parse.quote(nickname, safe='')
        full_url = f"{base_url}/info?name={encoded_name}&preset=00000"

        embed = discord.Embed(
            title=f"🔍 '{nickname}'의 환산 정보",
            description=f"캐릭터 정보는 아래 버튼을 눌러 확인하세요!",
            color=discord.Color.green()
        )
        embed.set_footer(text="Data by maplescouter.com")

        return embed, ScouterView(full_url)

    else:
        embed = discord.Embed(
            title="🧮 메이플 환산 사이트",
            description=f"전체 환산 사이트로 이동합니다.",
            color=discord.Color.blue()
        )
        embed.set_footer(text="Data by maplescouter.com")

        return embed, ScouterView(base_url)

def create_boss_embed_with_button(nickname: str = None):
    base_url = "https://maplescouter.com"

    if nickname:
        encoded_name = urllib.parse.quote(nickname, safe='')
        full_url = f"{base_url}/result?name={encoded_name}&preset=00000"

        embed = discord.Embed(
            title=f"💥 '{nickname}'의 보스 배율 정보",
            description="보스 배율 정보는 아래 버튼을 눌러 확인하세요!",
            color=discord.Color.red()
        )
        embed.set_footer(text="Data by maplescouter.com")

        return embed, ScouterView(full_url)

    else:
        embed = discord.Embed(
            title="💥 메이플 보스 배율 정보",
            description="보스 배율 사이트로 이동합니다.",
            color=discord.Color.orange()
        )
        embed.set_footer(text="Data by maplescouter.com")

        return embed, ScouterView(base_url)
