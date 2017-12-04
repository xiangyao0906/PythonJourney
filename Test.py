# coding=utf-8


# tile
def tile(str):
    print ("--------%s--------" % str)


# 换行
def nextLine():
    print("--------%s--------" % 'end')
    print("\r\n")


tile(str="Hello")
print "Hello world"
nextLine()

tile("for")
for i in range(0, 10, 1):
    if i == 9:
        print 'i的值是', i
    else:
        print 'i的值是', i,
nextLine()

tile("double for")
for i in range(0, 10, 1):
    for a in range(0, 3, 1):
        print '内循环', a,
    print '外循环', a
nextLine()

tile("yield 迭代器")


def fibonacci(n):
    a, b, conter = 0, 1, 0
    while True:
        if conter > n:
            return
        yield a
        a, b = b, a + b
        conter += 1


f = fibonacci(10)
for i in f:
    print i,


# 参数顺序,使用形参来传参可避免按顺序传递参数的问题
# 定义函数可以设置默认值

def introduce(name, age=20):
    print "传入的名字是 %s,今年%d" % (name, age)


introduce(name="aaa")
