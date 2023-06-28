
<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>
</p>

<div align="center">

# nonebot_plugin_d4boss


_✨ NoneBot d4boss查看插件 ✨_

</div>

<p align="center">
  <a href="https://raw.githubusercontent.com/cscs181/QQ-Github-Bot/master/LICENSE">
    <img src="https://img.shields.io/github/license/cscs181/QQ-Github-Bot.svg" alt="license">
  </a>
  <a href="https://pypi.python.org/pypi/nonebot_plugin_biliav">
    <img src="https://img.shields.io/pypi/v/nonebot_plugin_biliav.svg" alt="pypi">
  </a>
  <img src="https://img.shields.io/badge/python-3.7+-blue.svg" alt="python">
</p>

## 使用方式
发送:
d4b

返回：
世界BOSS为：The Wandering Death，距离刷新还有4分钟


## 定时任务
脚本同时也会启动一个定时任务，发送到具体的群号

```
@scheduler.scheduled_job("interval", minutes=1)
async def run_job():
    groupid = '12345' # 请手动配置该选项
    await job(groupid)
```