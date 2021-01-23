# 文件读写

# f = open('filedemo.txt')
# print(f.readable())
# print(f.readlines())
# f.close()

# with 语句块，可以将文件打开之后，操作完毕，自动关闭这个文件
# 图片读取需要使用rb  读取二进制的格式  with open('filedemo.txt', 'rb') as f:
# 正常的文本，可以使用rt，也就是它的默认格式
with open('filedemo.txt') as f:
    #print(f.readlines())

    while True:
        line = f.readline()
        if line:
            print(line)
        else:
            break