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
    # 分离奇数和偶数
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
