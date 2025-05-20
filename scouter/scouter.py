from discord.ext import commands
from scouter.scouter_logic import create_scouter_embed_with_button, create_boss_embed_with_button

def setup_commands(bot):
    @bot.command(name="환산", aliases=["스카우터"])
    async def scouter(ctx, nickname: str = None):
        embed, view = create_scouter_embed_with_button(nickname)
        await ctx.send(embed=embed, view=view)
        
    @bot.command(name="보스", aliases=["배율"])
    async def boss(ctx, nickname: str = None):
        embed, view = create_boss_embed_with_button(nickname)
        await ctx.send(embed=embed, view=view)