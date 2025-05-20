from discord.ext import commands
from azmoth.azmoth_logic import *

def setup_commands(bot):
    @bot.command()
    async def 가격(ctx):
        await maple_general_gold(ctx)

    @bot.command()
    async def 주화(ctx):
        await maple_general_gold(ctx)

    @bot.command()
    async def 손익(ctx):
        await maple_general_gold(ctx)

    @bot.command()
    async def maple(ctx, world: str = None, grade: str = None):
        if world and world not in valid_worlds:
            await ctx.send(f"오류: '{world}'는 유효한 서버명이 아닙니다.")
            return
        if grade and grade not in valid_grades:
            await ctx.send(f"오류: '{grade}'는 유효한 티어명이 아닙니다.")
            return

        try:
            alert_message = check_api_update_time()
            data = fetch_api_data()

            if data:
                if not world and not grade:
                    await send_all_data(ctx, data)
                elif world and not grade:
                    await send_server_data(ctx, data, world)
                else:
                    matching_data = [item for item in data if item['world'].lower() == world.lower() and item['name'].lower() == grade.lower()]
                    if matching_data:
                        info = matching_data[0]
                        maplepoint_value = calculate_meso_to_maplepoint(info['price'])
                        embed = create_embed(info, maplepoint_value, alert_message)
                        files = add_images(embed, grade_map[grade], world_map[world])
                        await ctx.send(embed=embed, files=files)
                    else:
                        await ctx.send(f"{world} 월드의 {grade} 등급 토큰 정보를 찾을 수 없습니다.")
            else:
                await ctx.send("API 요청에 실패했습니다.")
        except Exception as e:
            await ctx.send(f"오류 발생: {str(e)}")
