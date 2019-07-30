import requests
import discord
from discord import client
import os
import sys
import xml.etree.ElementTree as ET
import aiohttp
import io


class Main:
    TOKEN = '   '
    # BOTのトークン
    client = discord.Client()

    # クライアントの生成
    # デコレータ
    @client.event
    async def on_message(message):
        # Discordのbotはfuncごとにasyncが必要
        if message.author.bot:
            # もし発言したのがbotなら無視
            return
        if message.content == '/yndr':  #
            # もしメッセージがyndrなら～～
            imgurl = requests.get("https://yande.re/post.xml?limit=1")
            # yand.reから最新の投稿をget
            print("getting url")
            # logging
            root = ET.fromstring(imgurl.text)
            # XMLを準備
            r = requests.get(root.find("post").get("jpeg_url"), stream=True)
            # root.findで子要素の取得 .getでアブソリュート jpeg urlの取得
            print("get image")
            with open("temp.jpg", 'wb') as f:
                # 画像の一時保存
                f.write(r.content)
                # 保存
                print("saving file")
            await message.channel.send("` https://yande.re/post/show/" + root.find("post").get("id") + "`")
            await message.channel.send(file=discord.File('temp.jpg'))  # 投稿

            print("all work done")
            return
            # このままだと誤作動する可能性があるのでファイル名にtimestampを入れる必要あり
        if message.content == '/yndr -nocmpr':
            # 未圧縮ファイルモード レスポンスに難あり 処理は同じ、URLがpngになっただけ
            imgurl = requests.get("https://yande.re/post.xml?limit=1");
            print("getting url")
            root = ET.fromstring(imgurl.text)
            r = requests.get(root.find("post").get("file_url"), stream=True)
            print("get image")
            with open("temp.png", 'wb') as f:
                f.write(r.content)
                print("saving file")
            await message.channel.send(file=discord.File('temp.png'))
            print("all work done")
            return

    client.run(TOKEN)
    # すべての処理の記述が完了したので実行

    print("sex")
