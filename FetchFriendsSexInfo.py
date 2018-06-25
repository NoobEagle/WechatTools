# -*- coding: UTF-8 -*-
import itchat

itchat.auto_login()
# 爬取自己好友相关信息
friends = itchat.get_friends(update=False)

a = 0
manCount = 0
womenCount = 0
otherCount = 0
for f in friends:
    sex = f['Sex']
    if sex == 1:
        # 男性
        manCount += 1
    if sex == 2:
        womenCount += 1
    if sex == 3:
        otherCount += 1
    a += 1

# name = itchat.search_friends(name=u'菜鹰帅帅')
# XiaoMing = name[0]["UserName"]
itchat.send(str(a) + '位好友，' + str(manCount) + '位好友是男性,\n'
            # + str(womenCount) + "位好友是女性，还有" + str(otherCount) + "位好友处于中间地位", XiaoMing)
            + str(womenCount) + "位好友是女性，还有" + str(a - (manCount + womenCount)) + "位好友处于中间地位", 'filehelper')
print("完成")
