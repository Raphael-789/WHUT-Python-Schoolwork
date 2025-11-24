# 读取第一行输入，以空格分割并转换为整数列表
ls = list(map(int, input().split()))
# 读取第二行输入，作为要删除的整数n
n = int(input())

# 创建新列表，存储不等于n的元素（即删除所有n）
result = [x for x in ls if x != n]

# 判断结果列表是否与原列表长度length相同（即是否没有删除任何元素）
#len能够返回对象的长度或者元素个数
if len(result) == len(ls):
    print("NOT FOUND")
else:
    print(result)
