#map() 函数会接收一个函数和一个或多个可迭代对象（如列表、元组等）作为参数，返回一个迭代器,迭代器的每个元素都是将传入的函数应用到可迭代对象对应元素上的结果。
#简单来说就是“映射” 可迭代对象中的每个元素，通过指定的函数进行处理，然后返回处理后的新元素。
#如：map(function, iterable, ...)
#function：要应用于每个元素的函数。
#iterable：一个或多个可迭代对象（如列表、元组、字符串等）。
#返回值：一个 map 对象（迭代器），可以通过 list()、tuple() 等函数转换为具体的序列。
#示例
#1. 单个可迭代对象
#将列表中的每个元素平方：
def square(x):
    return x ** 2

nums = [1, 2, 3, 4]
result = map(square, nums)  # 返回 map 对象
print(list(result))  # 转换为列表输出：[1, 4, 9, 16]

#2. 多个可迭代对象
#将两个列表中对应位置的元素相加：
def add(x, y):
    return x + y

list1 = [1, 2, 3]
list2 = [10, 20, 30]
result = map(add, list1, list2)
print(list(result))  # 输出：[11, 22, 33]

#3. 使用匿名函数（lambda）
#简化代码，无需单独定义函数：
nums = [1, 2, 3, 4]
result = map(lambda x: x ** 2, nums)
print(list(result))  # 输出：[1, 4, 9, 16]

#4. 处理字符串
#将字符串中的每个字符转换为大写：
s = "hello"
result = map(lambda c: c.upper(), s)
print(''.join(result))  # 输出：HELLO

#join函数用法另附。基本格式：分隔符字符串.join(可迭代对象)
