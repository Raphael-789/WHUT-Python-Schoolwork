# 读取输入的学生数量n，并转换为整数类型
n = int(input())

# 判断n是否为正整数，如果不是，输出"ERROR"
if n <= 0:
    print("ERROR")
else:
    # 初始化一个空的二维列表，用于存储脱敏后的学生信息
    result = []
    
    # 循环n次，读取每个学生的信息
    for _ in range(n):
        # 读取一行学生信息，按空格分割为学号、姓名、电话号码
        student_id, name, phone = input().split()
        
        # 脱敏学号：第5-11位（索引4-10）改为*
        # 学号为13位或14位，切片前4位 + 7个* + 从第11位（索引11）开始的后续字符
        masked_id = student_id[:4] + '*' * 7 + student_id[11:]
        
        # 脱敏姓名：第2位改为*
        # 保留姓名第一个字符 + * + 从第3个字符（索引2）开始的后续字符（处理姓名长度大于2的情况）
        masked_name = name[0] + '*' + name[2:] if len(name) > 1 else name
        
        # 脱敏电话号码：第4-7位（索引3-6）改为*
        # 保留电话号码前3位 + 4个* + 从第7位（索引7）开始的后续字符
        masked_phone = phone[:3] + '*' * 4 + phone[7:]
        
        # 将脱敏后的学号、姓名、电话号码组成列表，添加到result二维列表中
        result.append([masked_id, masked_name, masked_phone])
    
    # 输出脱敏后的二维列表
    print(result)
