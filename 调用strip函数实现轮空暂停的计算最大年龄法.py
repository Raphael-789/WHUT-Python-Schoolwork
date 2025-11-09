# 初始化一个空列表，用于存储所有输入的出生日期字符串
dates = []

# 无限循环读取输入，直到用户输入空字符串（直接按回车）
while True:
    # 读取一行输入并去除首尾空白字符（处理可能的空格或制表符）
    #strip() 会去除换行符和可能的空格，确保空输入被正确识别为 ""，从而触发 break 退出循环。
    date = input().strip()
    
    # 判断输入是否为空字符串，若是则结束循环
    if not date:
        break
    
    # 将非空的日期字符串添加到列表中
    dates.append(date)

# 找出列表中最小的日期字符串（因yyyy-mm-dd格式天然按字典序排序，最小即最早/年龄最大）
oldest_date = min(dates)

# 输出年龄最大的出生日期
print(oldest_date)
