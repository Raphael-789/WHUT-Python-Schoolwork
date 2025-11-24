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

#布尔代数（Boolean Algebra）是 以布尔值（True 和 False）为基础，研究逻辑运算（与、或、非、异或等）规律的数学分支
#主要通过 布尔运算符 和 布尔表达式 实现，用于解决逻辑判断问题（如条件判断、循环控制、逻辑验证等）。


#1. 布尔值 (Boolean Values)
# 直接赋值布尔值
is_raining = True
has_umbrella = False

print(f"天在下雨吗? {is_raining}")
print(f"我有雨伞吗? {has_umbrella}")

# 布尔值的类型
print(f"is_raining 的类型是: {type(is_raining)}") # 输出: <class 'bool'>

# 布尔值与整数的关系 (True 是 1, False 是 0)
print(f"True + 1 = {True + 1}")  # 输出: 2
print(f"False * 10 = {False * 10}") # 输出: 0



#2.比较运算符 结果是一个布尔值。这是构建布尔表达式的基础。


x = 10
y = 5

# 等于 ==
print(f"{x} == {y} ? {x == y}")  # 输出: 10 == 5 ? False

# 不等于 !=
print(f"{x} != {y} ? {x != y}")  # 输出: 10 != 5 ? True

# 大于 >
print(f"{x} > {y} ? {x > y}")    # 输出: 10 > 5 ? True

# 小于 <
print(f"{x} < {y} ? {x < y}")    # 输出: 10 < 5 ? False

# 大于等于 >=
print(f"{x} >= {y} ? {x >= y}")  # 输出: 10 >= 5 ? True

# 小于等于 <=
print(f"{x} <= {y} ? {x <= y}")  # 输出: 10 <= 5 ? False


#3. 逻辑运算符 (布尔代数核心)用于组合布尔值，执行逻辑运算。
#与 或 非

#4.复杂布尔表达式与优先级：not > and > or。可以使用括号 () 来改变运算顺序。
# 场景: 判断一个学生的成绩是否优秀
# 优秀的条件是: (总分 > 90) OR (平均分 > 85 AND 没有不及格的科目)
total_score = 88
avg_score = 87
has_failed_subject = False

is_excellent = total_score > 90 or (avg_score > 85 and not has_failed_subject)

print(f"总分 > 90: {total_score > 90}")
print(f"平均分 > 85 且 没有不及格科目: {avg_score > 85 and not has_failed_subject}")
print(f"该学生是否优秀? {is_excellent}") # 输出: 该学生是否优秀? True

#5.布尔代数 最常见的用途就是在 if-else 条件判断语句中，根据条件的真假来执行不同的代码块。
age = 20
has_id = True

# 场景: 判断一个人是否可以进入酒吧
if age >= 18 and has_id:
    print("欢迎进入酒吧！") # 因为 age >= 18 和 has_id 都是 True，所以执行这里
else:
    print("抱歉，你不能进入。")

# 另一个例子
score = 75
if score >= 60:
    print("考试通过！")
else:
    print("考试失败，需要补考。")
