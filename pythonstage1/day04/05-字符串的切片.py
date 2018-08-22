# 字符串的切片 -> 其他语言字符串的截取

# 下标
# a = "abcdef"
# ret1 = a[1]

# 获取某个字符串中的字符串片段(字符串的子串) -> 切片
# 切片的语法：[起始:结束:步长] -> 默认[起始:结束] 步长等于1
# [起始:结束)

a = "abcdef"

# 'abc'
# [0:3] 或者 [:3]
# ret1 = a[:3]
# print(ret1)

# 'ace'
# ret2 = a[:5:2]
# print(ret2)

# 'bd'
# ret3 = a[1:4:2]
# print(ret3)

# 'fdb'
# ret4 = a[-1:-6:-2]
# print(ret4)

# 'fd'
# ret5 = a[-1:-4:-2]
# print(ret5)

# 如果"abcdef" 倒置 "fedcba"
# ret = a[::-1]
# print(ret)

# 切片技术使用的比较灵活 条条大路通罗马