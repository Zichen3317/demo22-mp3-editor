# -*- coding:utf-8 -*-
# ==========================================
#       Author: ZiChen
#        Mail: 1538185121@qq.com
#         Time: 2021/06/06
#           Version:
#             Description:
# ==========================================
import eyed3
version = '0.1'


def edit(path, artist, album, title):
    '''
    修改MP3歌曲信息
    path 歌曲路径
    artist 参与创作的艺术家
    album 唱片集
    title 标题
    '''
    audiofile = eyed3.load("%s" % path)
    audiofile.tag.artist = u"%s" % artist
    audiofile.tag.album = u"%s" % album
    audiofile.tag.title = u"%s" % title

    print("===修改完成===\n\
歌曲文件:%s \n\
参与创作的艺术家:%s \n\
唱片集:%s \n\
标题:%s \n" % (path, artist, album, title))
    audiofile.tag.save()
