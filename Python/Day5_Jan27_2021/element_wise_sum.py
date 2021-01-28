# For given, two list of integers. Find the elementwise sum

list1 = [1,2,3,4,5]
list2 = [4,2,5,2,5]

elementWiseSum = [sum(pair) for pair in zip(list1,list2)]
print(elementWiseSum)