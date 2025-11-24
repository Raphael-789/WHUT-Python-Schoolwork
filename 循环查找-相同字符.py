def longest_common_prefix(strs):
    # 如果列表为空，直接用return把字符串字面量返回给调用者函数longest_common_prefix
    if not strs:#如果莫得字符串
        return 'NOT FOUND'
    
    # 找到最短字符串的长度，前缀最长不会超过它
    min_length = min(len(s) for s in strs)
    common_prefix = []
    
    # 逐位比较所有字符串的对应字符
    for i in range(min_length):
        # = strs[0][i] 的作用是获取列表中第一个字符串的第 i 个字符，作为后续比较的 “基准字符”.
        # 取第一个字符串的第i个字符作为基准
        current_char = strs[0][i]
        # 检查其他所有字符串的第i个字符是否与基准相同
        for s in strs[1:]:
            if s[i] != current_char:
                # 有不同则停止比较
                if not common_prefix:
                    return 'NOT FOUND'
                else:
                    return ''.join(common_prefix)
        # 所有字符串第i位相同，加入前缀列表
        common_prefix.append(current_char)
    
    # 所有最短长度内的字符都相同，返回拼接结果
    #将列表 common_prefix 中的所有字符拼接成一个完整的字符串
    #并将这个字符串作为函数的返回值
    return ''.join(common_prefix)

# 读取输入并分割为字符串列表
input_strs = input().split()
# 调用函数并输出结果
print(longest_common_prefix(input_strs))
