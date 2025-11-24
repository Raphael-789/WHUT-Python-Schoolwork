# 读取输入并转换为整数列表
try:
    A = list(map(int, input().split()))
except ValueError:
    print("ERROR")
    exit()

# 检查列表长度是否为偶数（奇数和偶数各占一半，总长度必须是偶数）
if len(A) % 2 != 0:
    print("ERROR")
else:
    # 分离奇数和偶数。
    #用到列表推导式（List Comprehension），基本语法是：[表达式 for 变量 in 可迭代对象 if 条件]
    odds = [x for x in A if x % 2 != 0]
    evens = [x for x in A if x % 2 == 0]
    
    # 验证奇数和偶数数量是否相等
    if len(odds) != len(evens):
        print("ERROR")
    else:
        # 分别排序
        odds.sort()
        evens.sort()
        #对列表中的元素进行原地排序（即直接修改原列表，不会创建新列表）
        
        # 重新组合：偶数索引放偶数，奇数索引放奇数
        result = []
        for i in range(len(evens)):
            result.append(evens[i])  # 偶数索引（0,2,4...）
            result.append(odds[i])   # 奇数索引（1,3,5...）
        
        print(result)




#Version2：传统循环写法


A = [1, 2, 3, 4, 5, 6]

# 分离奇数 (等价于列表推导式)
odds = []
for x in A:
    if x % 2 != 0:
        odds.append(x)

# 分离偶数 (等价于列表推导式)
evens = []
for x in A:
    if x % 2 == 0:
        evens.append(x)

print(odds)  # 输出: [1, 3, 5]
print(evens) # 输出: [2, 4, 6]



#try是什么？ “尝试” 执行一段可能出错的代码，如果出错了，就 “捕获” 这个错误，并执行一些备用逻辑。
#try 通常与 except 配合使用，构成 try...except 语句块。

try:
    # 尝试执行的代码块
    # 这里的代码可能会抛出异常
    risky_operation()

except SomeSpecificError:
    # 当 try 块中抛出 SomeSpecificError 类型的异常时，执行这里的代码
    # 这是处理该特定错误的逻辑
    handle_error()

except AnotherSpecificError:
    # 可以有多个 except 块，分别处理不同类型的异常
    handle_another_error()

except Exception as e:
    # 捕获所有其他类型的异常（不推荐，但有时有用）
    # 'e' 变量会包含异常的详细信息
    print(f"发生了未知错误: {e}")

else:
    # (可选) 如果 try 块中的代码没有抛出任何异常，执行这里的代码
    print("一切正常！")

finally:
    # (可选) 无论 try 块是否抛出异常，这里的代码总会执行
    # 通常用于资源清理，如关闭文件、数据库连接等
    cleanup_resources()

#举个例子：
filename = "nonexistent_file.txt"

try:
    # 尝试打开并读取文件
    with open(filename, "r") as file:
        content = file.read()
    print(f"文件内容: {content}")

except FileNotFoundError:
    # 专门处理文件不存在的错误
    print(f"错误：文件 '{filename}' 不存在。")

except IOError as e:
    # 处理其他 I/O 相关错误，如权限问题等
    print(f"读取文件时发生 I/O 错误: {e}")

except Exception as e:
    # 捕获其他所有未预料到的错误
    print(f"发生了一个意外错误: {e}")

finally:
    # 这个块总会执行，即使前面的代码都失败了
    print("文件操作尝试完毕。")
