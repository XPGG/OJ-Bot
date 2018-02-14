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
    choco = ['!チョコ','!チョコレート']
    args = message.content.split(' ') 
    if not message.author.bot:
        if message.content.startswith("おは"):
            m = "おはようですわよ" + message.author.name + "嬢！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await client.send_message(message.channel, m)
        elif message.content in choco:
            # メッセージを書きます
            m = "私の手作りチョコ受け取って貰えるかしら？" + message.author.name + "嬢。"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await client.send_message(message.channel, m)
        elif message.content.startswith("!mcnow "):
            server_name = message.content[7:]
            server_info = "<@%s> %s" % (message.author.id, minecraft_server_info.get_server_info(server_name))
            await client.send_message(message.channel, server_info)
        elif message.content.startswith("!dice "):
            dice.set_dice(args)#Dice型インスタンスにダイスの生文字列をセットしてやるわよ
            await client.send_message(message.channel, dice.throw_dice())
            #throw = message.content[6:]
            #diced = "<@%s> %s" % (message.author.id, dice.get_dice(throw))
            #await client.send_message(message.channel, diced)
        elif message.content in utages:
            await client.delete_message(message)
            # メッセージを書きます
            m = "I am シャイボーイ i am tokyo(福岡)"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            response = await client.send_message(message.channel, m)
            await asyncio.sleep(5)
            await client.delete_message(response)



client.run(settings.token)
