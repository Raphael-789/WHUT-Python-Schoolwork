#Python 字符串的切片语法，[::-1] 表示从尾到头取所有字符.
#切片语法(Slice)是提取序列的部分元素，适用于字符串、列表、元组等。
#核心格式为[start:end:step]
#支持负数：末尾开始/末尾索引/反向截取
#一般常用省略参数而非基础截取：从开头/到末尾

import math  # 导入math模块，用于计算平方根，优化素数判断效率

def is_prime(num):
    """判断一个数是否为素数"""
    if num < 2:  # 小于2的数不是素数
        return False
    # 检查从2到num平方根之间的数是否能整除num，若能则不是素数
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True  # 若没有能整除的数，则是素数

def is_palindrome(num):
    """判断一个数是否为回文数（正反读相同）"""
    s = str(num)  # 将数字转为字符串
    return s == s[::-1]  # 比较字符串与反转后的字符串是否相同

n = int(input())  # 读取输入的正整数n
anti_primes = []  # 用于存储找到的反素数

# 遍历2到n-1的所有数（因为反素数至少是两位数，且小于n）
for num in range(2, n):
    if is_prime(num):  # 先判断当前数是否为素数
        # 生成当前数的反转数（如13反转为31）
        #Python 字符串的切片语法，[::-1] 表示从尾到头取所有字符
        reversed_num = int(str(num)[::-1])
        # 反素数条件：反转数也是素数，且原数不是回文数（反转数≠原数）
        if reversed_num != num and is_prime(reversed_num):
            anti_primes.append(str(num))  # 将符合条件的数转为字符串存入列表

# 按要求格式输出结果（每个数字后带空格）
print(' '.join(anti_primes) + ' ')
