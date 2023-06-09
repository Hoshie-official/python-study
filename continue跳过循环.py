num = 0
sum = 0
while num <= 1000:
    num = num + 1
    if num % 2 == 1:
        continue
    sum = sum + num
print(sum)
#continue跳过后续循环代码，继续下一次循环
