T = (100, 69, 29, 100, 72, 99, 98, 100, 75, 100, 100, 42, 88, 100)
m = T.count(100)
# count()方法用来统计tuple中某个元素出现的次数。
# 对于不存在的元素，count方法不会报错，而是返回0，这是合理的，因为元组里面有0个不存在的元素。
print(m)
# index()方法可以返回指定元素的下标，当一个元素多次重复出现时，则返回第一次出现的下标位置。
#当指定的元素不存在时，使用index()方法Python会报错。
