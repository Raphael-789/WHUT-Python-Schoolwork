#输入为一个正整数 n，题目保证 0 < n <= 1000 。
n = int(input())

#定义一个空列表solutions用于存储所有满足条件的物品个数（后续找到符合条件的数时，会添加到这个列表中）。

solutions = []

# 遍历1到n的所有整数，检查是否满足 “物不知数” 的条件
#append  v. （在文章后面）附加；添加；补充；添写；增补
for m in range(1, n + 1):
    if m % 3 == 2 and m % 5 == 3 and m % 7 == 2:
        solutions.append(m)

# 根据是否有解输出相应结果
if solutions:
    for num in solutions:
        print(num)
else:
    print("No solution!")
