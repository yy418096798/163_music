from tkinter import *
import requests
from lxml import etree
import re
from urllib.request import urlretrieve


def DownMusic():
    # http://music163.com/song/media/outer/url?id=
    # https://music.163.com/playlist?id=2602222983
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    url = enter.get()
    url = url.replace("/#", "")
    # print(url)
    response = requests.get(url, headers = headers)
    response.encoding = response.apparent_encoding
    html = response.text
    # print(html)
    tree = etree.HTML(html)
    song_name = tree.xpath('//ul[@class="f-hide"]/li/a/text()')
    song_id = tree.xpath('//ul[@class="f-hide"]/li/a/@href')
    music_id = []
    for i in song_id:
        id = re.findall("=(\d+)", i, re.S)
        music_id.append(id)
    # print(len(music_id))
    # print(len(song_name))

    for s, name in zip(music_id, song_name):
        s = s[0]
        print(s, name)
    #     # url2 = "http://music.163.com/song/media/outer/url?id=317151.mp3"
    #     url2 = "http://music.163.com/song/media/outer/url?id=%s.mp3" % s

    #     r = requests.get(url2, headers = headers)
    #     # r.encoding = r.apparent_encoding
    #     # html1 = r.text
    #     # tree1 = etree.HTML(html1)
    #     # href = tree1.xpath("//source")
    #     # print(html1)
    #     # break
    #     with open(name+".mp3", "wb") as f:
    #         f.write(r.content)
    #     text.insert(END,"正在下载： "+name)
    #     text.see(END)
    #     text.update()
    #
    # text.insert(END,"Complete")

# 创建窗口
root = Tk()
# 设置标题
root.title("网易云音乐")
# 设置窗口默认大小（横向长度x纵向长度）
root.geometry("550x400")
# 调整窗口出生位置(+横向坐标+纵向坐标)
root.geometry("+300+120")
# 创建标签空间
Lable = Label(root, text = "请输入歌单url：", font = ("宋体"))
# 定位标签    grid 网格式布局     pack 包      place 位置
Lable.grid()
# 创建输入框
enter = Entry(root, font = ("黑体"),width = 38)
# 表格式布局，row 第0行、column 第1列
enter.grid(row = 0, column = 1)
# 列表框控件
text = Listbox(root, font = ("华文行楷", 20), width = 45, height = 11)
# columnspan 组件所跨越的列数
text.grid(row = 1, columnspan = 2)
# 开始按钮
button1 = Button(root,text = "开始", width = 10, command = DownMusic)
# 开始按钮定位，对齐方式：左对齐（N、S、W、E -- 上下左右）
button1.grid(row = 2, column = 0, sticky = W)
# 退出按钮
button2 = Button(root, text = "退出", width = 10, command = root.quit)
# 退出按钮定位，对齐方式：左对齐（N、S、W、E -- 上下左右）
button2.grid(row = 2, column = 1, sticky = E)
# 显示窗口, 消息循环
root.mainloop()
