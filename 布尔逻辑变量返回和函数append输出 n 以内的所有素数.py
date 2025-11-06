#输出 n 以内的所有素数

import math

n = int(input())
primes = []
for num in range(2, n + 1):
    
#遍历从 2 到 n 的所有整数生成序列），num依次代表判断数。
    
    is_prime = True

#定义一个逻辑上的布尔变量is_prime，先假设它是质数
#一个布尔变量最好只负责一个状态
#（如is_prime标记是否为质数、found标记是否找到目标）
#在嵌套结构中，布尔值在不同层级传递状态，实现逻辑控制。

    sqrt_num = int(math.sqrt(num)) + 1

#math.sqrt(num)计算num的平方根并取整数部分
    
    for i in range(2, sqrt_num):
        if num % i == 0:
            is_prime = False
            break
#若满足上一行的条件（num能被i整除），则将is_prime设为False，标记num不是质数。
#一旦找到能整除num的i，就跳出当前的内层循环（无需继续判断更大的i）。
        
    if is_prime:
        primes.append(str(num))

#内层循环结束后，判断is_prime是否仍为True。
    #若是，说明num在 2 到sqrt_num-1之间没有任何除数，即num是质数。

#append()用于向数据结构（如列表、集合和字典）中添加元素。
        
#str() 是 Python 的一个内置函数，用于将对象转换为字符串形式。
#它非常实用，尤其是在需要将非字符串类型的数据（如数字、列表、字典等）转换为字符串时。


print(' '.join(primes) + ' ')
