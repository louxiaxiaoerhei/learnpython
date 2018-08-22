import re


my_path = "c:\\a\\b\\c"
print(my_path)


# match_obj = re.match("c:\\\\a\\\\b\\\\c", my_path)

# r: 表示原始字符串，正则表达式里面的反斜杠以后不需要再进行转义，只针对与反斜杠
match_obj = re.match(r"c:\\a\\b\\c", my_path)
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")


match_obj = re.match(r"<([a-zA-Z1-6]+)>.*</\1>", "<html>hh</html>")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")

# 建议: 如果使用使用正则表达式匹配数据可以都加上r，要注意r针对的只是反斜杠起作用，不需要对其进行转义