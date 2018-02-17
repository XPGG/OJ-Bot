import discord
import settings
import minecraft_server_info
import dice2
import asyncio

client = discord.Client()
dice = dice2.Dice()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    utages = ['!うたげ', '!utage', '!ウタゲ']
    args = message.content.split(' ')
    if not message.author.bot:
        if message.content.startswith("おは"):
            m = "おはようですわよ" + message.author.name + "嬢！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await client.send_message(message.channel, m)
        elif message.content.startswith("オフ会"):
            # メッセージを書きます
            m = "オフ会楽しみですわね！" + message.author.name + "嬢！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await client.send_message(message.channel, m)
        elif message.content.startswith("!mcnow "):
            server_name = message.content[7:]
            server_info = "<@%s> %s" % (message.author.id, minecraft_server_info.get_server_info(server_name))
            await client.send_message(message.channel, server_info)
        elif message.content.startswith("!dice "):
            dice.set_dice(args)
            await client.send_message(message.channel, "<@%s> 嬢へ %s" % (message.author.id, dice.throw_dice()))
        elif message.content in utages:
            await client.delete_message(message)
            # メッセージを書きます
            m = "I am シャイボーイ 恋心はマーマレードのよう。"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            response = await client.send_message(message.channel, m)
            await asyncio.sleep(5)
            await client.delete_message(response)


client.run(settings.token)
