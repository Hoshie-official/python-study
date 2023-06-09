num = 0
sum = 0
while True:
    if num > 1000:
        break
    if num % 2 == 0:
        sum = sum + num
    num = num + 1
print(sum)
