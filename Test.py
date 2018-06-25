import itchat

itchat.auto_login(hotReload=True)
# 爬取自己好友相关信息
friends = itchat.get_friends(update=False)

b = 0
a = 0
provinceCount = 0
provinceList = []
provinceMap = {}
for f in friends:
    b = a + 1
    province_ = f['Province']
    if province_ == '':
        province_ = '未知'
    if (provinceList.__contains__(province_) == False):
        provinceCount = provinceCount + 1
        provinceList.append(province_)
        provinceMap[province_] = 1
    else:
        provinceMap[province_] = provinceMap[province_] + 1
    a += 1

l = sorted(provinceMap.items(), key=lambda e: e[1], reverse=True)
text2 = str(l)
text = str(provinceList)
itchat.send(str(a) + '位好友，共来自' + str(provinceCount) + '个城市,\n' + text2, 'filehelper')
print("完成")
