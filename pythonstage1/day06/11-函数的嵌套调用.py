# 定义一个函数
def func1():
    print("func1开始")
    print("func1")
    print("func1结束")

# 定义一个函数
def func2():
    print("func2开始")
    func1()
    print("func2结束")

# 定义一个函数
def func3():
    print("func3开始")
    func2()
    print("func3结束")

# print("程序开始")
# func3()
# print("程序结束")

"""
程序开始
func3开始
func2开始
func1开始
func1
func1结束
func2结束
func3结束
程序结束

程序开始
func3开始
func2开始
func1开始
func1
func1结束
func2结束
func3结束
程序结束
"""

# 扩展
def func4():
    def func5():
        print("你好")

    func5()
func4()