
# %2d 代表占位两位 如果位数不足 使用空格占位
# %2d 右对齐
# %-2d 左对齐
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d * %d = %-4d" % (j, i, j * i), end="")
        j += 1
    print()
    i += 1


# j = 1
# while j <= 5:
#     print(j, end="")
#     j += 1