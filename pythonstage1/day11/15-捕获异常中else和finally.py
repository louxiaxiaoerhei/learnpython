num = 10
# 捕获异常
try:
    print(num)
except:
    print("except")
else:
    print("else")
finally:
    print("finally")

# 使用捕获异常技术
# 如果try中的代码发生异常 -> except -> finally
# 如果try中的代码没有发生异常 -> else -> finally

# import pygame
# pygame.init()