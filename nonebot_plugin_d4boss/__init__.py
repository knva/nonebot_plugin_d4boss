import time
import httpx
from nonebot import on_command
import nonebot
from nonebot.rule import startswith
from nonebot.adapters.cqhttp import Bot, Event
import quxiaoxi.cq as cq, json
from nonebot.adapters.cqhttp import MessageSegment, Message, Bot, Event
from nonebot import get_bot

from nonebot import require


require("nonebot_plugin_apscheduler")


from nonebot_plugin_apscheduler import scheduler

__usage__ = '使用方法：\n' \
            'd4b'


__version__ = '0.1.1'

__plugin_name__ = "d4boss"
dg = on_command("d4b", rule=startswith("d4b"))


@dg.handle()
async def firsthandle(bot: Bot, event: Event, state: dict):

    async with httpx.AsyncClient() as client:
        response = await client.get('https://d4armory.io/api/events/recent')
        if response.status_code != 200:
            await dg.finish("你说得对，但是暗黑破坏神4是一款由动视暴雪开发的，中间忘了，一起探索庇护之地的真相！")
        try:
            data = response.json()
            boss_data = data['boss']
            print(boss_data)
            boss_name = boss_data['name']
            boss_expected = boss_data['expected']
        except:
            print("Request failed, status code " + str(response.status_code))
            await dg.finish("你说得对，但是暗黑破坏神4是一款由动视暴雪开发的，中间忘了，一起探索庇护之地的真相！")

        current = time.time()
        print(current)

        diff = boss_expected - current
      
        await  dg.finish("世界BOSS为：{}，距离刷新还有{}分钟".format(boss_name, int(diff/60)))

async def job(groupid):
      async with httpx.AsyncClient() as client:
        response = await client.get('https://d4armory.io/api/events/recent')
        try:
            data = response.json()
            boss_data = data['boss']
            print(boss_data)
            boss_name = boss_data['name']
            boss_expected = boss_data['expected']
        except:
            print("Request failed, status code " + str(response.status_code))
      
        current = time.time()
        print(current)

        diff = boss_expected - current
        # 如果还剩五分钟就提醒
        if diff < 300:
            bot = get_bot()
            msg = "请注意，世界BOSS为：{}，距离刷新还有{}分钟".format(boss_name, int(diff/60))
            await bot.send_group_msg(group_id=groupid, message=msg)
            # await  dg.finish()


@scheduler.scheduled_job("interval", minutes=1)
async def run_job():
    groupid = '12345' # 请手动配置该选项
    await job(groupid)