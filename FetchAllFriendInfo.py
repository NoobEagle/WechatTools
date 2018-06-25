import time
import itchat
import xlwt

itchat.auto_login(hotReload=True)

# 爬取自己好友相关信息
friends = itchat.get_friends(update=False)

# 创建表格
file = xlwt.Workbook()
table = file.add_sheet('info', cell_overwrite_ok=True)
# 创建第一行的字段描述
# table.write(行数, 列数, '内容')
table.write(0, 0, 'MemberList')
table.write(0, 1, 'Uin')
table.write(0, 2, 'UserName')
table.write(0, 3, 'NickName')
table.write(0, 4, 'HeadImgUrl')
table.write(0, 5, 'ContactFlag')
table.write(0, 6, 'MemberCount')
table.write(0, 7, 'RemarkName')
table.write(0, 8, 'HideInputBarFlag')
table.write(0, 9, 'Sex')
table.write(0, 10, 'Signature')
table.write(0, 11, 'VerifyFlag')
table.write(0, 12, 'OwnerUin')
table.write(0, 13, 'PYInitial')
table.write(0, 14, 'PYQuanPin')
table.write(0, 15, 'RemarkPYInitial')
table.write(0, 16, 'RemarkPYQuanPin')
table.write(0, 17, 'StarFriend')
table.write(0, 18, 'AppAccountFlag')
table.write(0, 19, 'Statues')
table.write(0, 20, 'AttrStatus')
table.write(0, 21, 'Province')
table.write(0, 22, 'City')
table.write(0, 23, 'Alias')
table.write(0, 24, 'SnsFlag')
table.write(0, 25, 'UniFriend')
table.write(0, 26, 'DisplayName')
table.write(0, 27, 'ChatRoomId')
table.write(0, 28, 'KeyWord')

b = 0
a = 0
for f in friends:
    b = a + 1
    table.write(b, 0, f['MemberList'])
    table.write(b, 1, f['Uin'])
    table.write(b, 2, f['UserName'])
    table.write(b, 3, f['NickName'])
    table.write(b, 4, f['HeadImgUrl'])
    table.write(b, 5, f['ContactFlag'])
    table.write(b, 6, f['MemberCount'])
    table.write(b, 7, f['RemarkName'])
    table.write(b, 8, f['HideInputBarFlag'])
    table.write(b, 9, f['Sex'])
    table.write(b, 10, f['Signature'])
    table.write(b, 11, f['VerifyFlag'])
    table.write(b, 12, f['OwnerUin'])
    table.write(b, 13, f['PYInitial'])
    table.write(b, 14, f['PYQuanPin'])
    table.write(b, 15, f['RemarkPYInitial'])
    table.write(b, 16, f['RemarkPYQuanPin'])
    table.write(b, 17, f['StarFriend'])
    table.write(b, 18, f['AppAccountFlag'])
    table.write(b, 19, f['Statues'])
    table.write(b, 20, f['AttrStatus'])
    table.write(b, 21, f['Province'])
    table.write(b, 22, f['City'])
    table.write(b, 23, f['Alias'])
    table.write(b, 24, f['SnsFlag'])
    table.write(b, 25, f['UniFriend'])
    table.write(b, 26, f['DisplayName'])
    table.write(b, 27, f['ChatRoomId'])
    table.write(b, 28, f['KeyWord'])
    a += 1

fileName = 'weixin_' + time.strftime("%Y%m%d", time.localtime()) + '.xls'
file.save(fileName)
itchat.send('@%s@%s' % ('fil', fileName), 'filehelper')
print("完成")
