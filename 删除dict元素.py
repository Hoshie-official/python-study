d = {
    'Alice': 45,
    'Bob': 60,
    'Candy': 75,
    'David': 86,
    'Ellena': 49
}
p = d.keys()


# if d.get('Alice') is None:
#    print(d)
# else:
#    alice = d.pop('Alice')
#    print(alice)
#    print(d)
# 这是我自己写的，实际上是直接从dict里判断指定的key是否为空了，这个方法其实不可取
# 实际上应该查询指定key是否在keys列表里

n = 'Alice'
if n in p:
    d.pop(n)
else:
    print('{} not in d'.format(n))

# 这里是用if来判断'Alice'是否在d.keys()里面
# 这个in我不记得了，没想到这么简单就行……
# 如果在的话就用d.pop()来删除这个key，这里应该是还能返回这个key的value的
# 如果不在，这里的print语句里面也有点意思，说实话可能之前学过但我忘了
# '{}'——这个大括号会输出Alice，应该是得益于format()
# 好像是学过，format会按顺序把值填入前面的大括号位置。
