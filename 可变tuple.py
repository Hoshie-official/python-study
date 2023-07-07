T = (1, 'CH', [3, 4])
L = T[2]
print(L) # ==> [3, 4]
# 尝试替换L中的元素
L[1] = 40
print(L) # ==> [3, 40]
print(T) # ==> (1, 'CH', [3, 40])
# 这是因为虽然tuple中的list元素改变了，但是tuple本身指向的list仍然是同一个list，
# list本身并没有改变，改变的只是list里面的一个元素，这是tuple所约束不到的范围。
