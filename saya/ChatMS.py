# import requests
# import json
# import random

# from graia.application import GraiaMiraiApplication
# from graia.saya import Saya, Channel
# from graia.saya.builtins.broadcast.schema import ListenerSchema
# from graia.application.event.messages import *
# from graia.application.event.mirai import *
# from graia.application.message.elements.internal import *
# from graia.scheduler.saya.schema import SchedulerSchema
# from graia.scheduler.timers import crontabify

# from config import yaml_data, group_data


# saya = Saya.current()
# channel = Channel.current()

# root = {}


# @channel.use(SchedulerSchema(crontabify("* * 0 * * *")))
# def updateDict():
#     global root
#     root = json.loads(requests.get(
#         "https://raw.fastgit.org/Kyomotoi/AnimeThesaurus/main/data.json"
#     ).text)
#     print(f"已更新完成聊天词库")
#     print(f"共计：{len(root)}条")


# @channel.use(ListenerSchema(listening_events=[GroupMessage]))
# async def main(app: GraiaMiraiApplication, group: Group, message: MessageChain):

#     if yaml_data['Saya']['ChatMS']['Disabled']:
#         return
#     elif 'ChatMS' in group_data[group.id]['DisabledFunc']:
#         return

#     if message.has(At):
#         if message.getFirst(At).target == yaml_data['Basic']['MAH']['BotQQ']:
#             saying = message.getFirst(Plain).text
#             for key in root:
#                 if key in saying:
#                     return await app.sendGroupMessage(group, MessageChain.create([
#                         Plain(random.choice(root[key])),
#                         Plain(f"\n\n聊天处于测试阶段，谨慎使用。触发关键词：{key}"),
#                         # Plain(f"\nhttps://github.com/Kyomotoi/AnimeThesaurus/blob/main/data.json")
#                     ]))


# @channel.use(ListenerSchema(listening_events=[FriendMessage]))
# async def main(app: GraiaMiraiApplication, friend: Friend, message: MessageChain):
#     saying = message.getFirst(Plain).text
#     for key in root:
#         if key in saying:
#             return await app.sendFriendMessage(friend, MessageChain.create([
#                 Plain(random.choice(root[key])),
#                 # Plain(f"\n\n聊天处于测试阶段，谨慎使用。触发关键词：{key}"),
#                 # Plain(f"\nhttps://github.com/Kyomotoi/AnimeThesaurus/blob/main/data.json")
#             ]))

# updateDict()