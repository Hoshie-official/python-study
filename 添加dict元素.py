d = {
    'Alice': [45],
    'Bob': [60],
    'Candy': [75],
}
d['Alice'].extend([50, 61, 66])
d['Bob'].extend([80, 61, 66])
d['Candy'].extend([88, 75, 90])
print(d)
# dict和tuple不一样，dict是可变的，我们随时可以往dict中添加新的key-value
# 实际上，value可以是任意类型的元素，可以是list、tuple等，
# 可以用append()来添加单个元素
# 经过自行查找我发现了extend()，可以一次性添加多个元素
# 本质上应该是新建一个list，然后将新的list加入到旧list的末尾
# 赋值语句其实有两个功能：
# 当key不存在时，往dict中添加对应的key: value元素。
# 当key存在时，会更新dict，用新的value替换原来的value。
# 题外话，获取值的时候最好用get()，而不是直接赋值。这应该算是一种好习惯……吧？
