L = [[1,2,3], [5, 3, 2], [7,3,2]]
#第一个列表是三个长方体的长，第二个列表是它们的宽，第三个是它们的高
for cube in L:
    length = cube[0]
    width = cube[1]
    height = cube[2]
    result = length * width * 2 + width * height * 2 + length * height * 2
    print(result)
    #对于二维list，列表里面的每一个元素仍然是一个列表
