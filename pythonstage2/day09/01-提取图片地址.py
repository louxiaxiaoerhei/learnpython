import re

my_url = '''<img alt="撒个蕉的直播" data-original="https://rpic.douyucdn.cn/asrpic/180814/1898003_4881225_2b8f5_1_1439.jpg" src="https://rpic.douyucdn.cn/asrpic/180814/1898003_4881225_2b8f5_1_1439.jpg" width="283" height="163" class="JS_listthumb" style="display: block;">'''

# 正则表达式默认是贪婪的，根据正则表达式尽量多匹配数据
# 非贪婪： 根据正则表达式是少匹配数据，?后面的数据不让前面的正则表达式匹配，留给?后面自己进行匹配
# 非贪婪的表现形式： +?, *?, ??
match_obj = re.search(r"https?://.+?\.jpg", my_url)

if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")

match_obj = re.match("#.*?#", "#sd#f#")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")