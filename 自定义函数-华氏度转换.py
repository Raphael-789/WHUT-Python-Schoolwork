# 定义华氏温度转摄氏温度的函数F to C
def F2C(f):
    # 使用公式计算摄氏温度：C=5×(F−32)/9
    c = 5 * (f - 32) / 9
    # 返回保留两位小数的结果
    return round(c, 2)

# 读取输入的两个华氏温度，按逗号分割并转换为整数
#input().split(',')读取多个输入值，按照指定分隔符分割（如上一个时间转换程序用的是：作为分隔符）
#默认分隔符sep=None, maxsplit=-1, 无限制分隔。
#分隔符可空可逗
f_input = input('输入逗号区间').split(',')
f1 = int(f_input[0])
f2 = int(f_input[1])

# 判断如果f1大于f2，输出error
if f1 > f2:
    print("error")
else:
    # 从f1开始，每次增加2，直到不超过f2
    for f in range(f1, f2 + 1, 2):
        # 调用转换函数得到摄氏温度
        c = F2C(f)
        # 格式化输出，确保摄氏温度显示两位小数
        print(f"{f} : {c:.2f}")
