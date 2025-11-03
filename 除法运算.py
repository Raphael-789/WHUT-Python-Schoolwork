# 读取输入的两个实数

a = float(input())
b = float(input())

# 判断除数是否为零

if b == 0:
    print("除零错误")
    
else:
    # 计算除法结果并四舍五入保留2位小数
    
    result = a / b
    
    #"{0:.2f}" 是格式化字符串的模板，其中：
    
    #0 表示要格式化的第一个参数（这里对应 result）；
    #:.2f 表示将该参数以浮点数形式显示，并且保留 2 位小数（会自动四舍五入）。
    #.format(result) 是将 result 的值传入模板中，替换 {0} 的位置。
    
    print("{0:.2f}".format(result))
