num = 0
L = ['Alice', 66, 'Bob', True, 'False', 100]
for item in L:
    num = num + 1
    if num % 2 != 0:  #!=，不等于，这个跟别的语言好像也都一样
        continue      #如果是奇数就跳过这个循环后续的操作，重新从头进入下一次循环
    print(item)       #输出列表中偶数位置的元素
