# -*- coding:utf-8 -*-
# ==========================================
#       Author: ZiChen
#        Mail: 1538185121@qq.com
#         Time: 2021/06/06
#           Version: 0.1
#             Description: MP3编辑
# ==========================================
import MP3Edit
import configparser
#  实例化configParser对象
config = configparser.ConfigParser()
# 读取配置文件
configPath = input("请输入配置文件路径:\n")
config.read(configPath, encoding='utf-8')
while True:
    path = input("请输入需要修改的歌曲(mp3)路径:\n")
    artist = config.get('data', 'artist')
    album = config.get('data', 'album')
    title = config.get('data', 'title')
    MP3Edit.edit(path, artist, album, title)
