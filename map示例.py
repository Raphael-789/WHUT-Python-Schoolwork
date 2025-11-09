# 定义一个列表（可迭代对象）
str_list = ['1', '2', '3', '4']

# 用 map 把 int 函数应用到每个元素上
int_iter = map(int, str_list)  # 返回一个迭代器

# 转换为列表查看结果
result = list(int_iter)
print(result)  # 输出：[1, 2, 3, 4]
