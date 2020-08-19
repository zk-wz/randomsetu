import asyncio
import random
from pathlib import Path
from graia.application import GraiaMiraiApplication, Session
from graia.application.message.chain import MessageChain
from graia.application.group import Group
from graia.broadcast import Broadcast
from graia.application.message.elements.internal import Image
loop = asyncio.get_event_loop()

bcc = Broadcast(loop=loop)
app = GraiaMiraiApplication(
    broadcast=bcc,
    connect_info=Session(
        host="http://0.0.0.0:8080", # 填入 httpapi 服务运行的地址
        authKey="123456", # 填入 authKey
        account=123456789, # 你的机器人的 qq 号
        websocket=True # Graia 已经可以根据所配置的消息接收的方式来保证消息接收部分的正常运作.
    )
)

@bcc.receiver("GroupMessage")
async def group_message_handler(app: GraiaMiraiApplication, message: MessageChain, group: Group):
    if message.asDisplay().startswith("色图"):
        await app.sendGroupMessage(group, MessageChain.create([
            await Image.fromNetworkAddress('https://cdn.jsdelivr.net/gh/zk-wz/randomsetu/piccache/  ('+str(random.randrange(1,281))+').jpg')
        ]))


app.launch_blocking()
