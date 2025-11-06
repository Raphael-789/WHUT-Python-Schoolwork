import math
#pi = math.pi

#要是你不知道math库里的定义函数：
#交互式环境情况：
#就用help(math.函数名)。
#或者直接查询整个库。
#终端命令：
#使用pydoc工具（python内置标准库）。
#[func for func in dir(math) if not
#func.startswith('_')]
#需要先引入math库


R = 6371 * 1000
# 1. 计算地球表面积（表面积公式S = 4πR2）
surface_area = 4*math.pi*R**2
print(f'地球表面积为{surface_area:.2f}平方米')

# 2. 计算地球体积（体积公式是V = 4πR3/3）
volume = (4*math.pi*R**3)/3
print(f'地球体积为{volume:.2f}立方米')

# 3. 计算地球赤道的周长（圆周长公式是L = 2πR）
circumference = 2*math.pi*R
print(f'地球赤道周长为{circumference:.2f}米')

# 4.计算绳子与地球之间的空隙大小
delta = 1 # 绳子延长 1 米
gap = delta / (2 * math.pi)
print(f'空隙大小为{gap:.2f}米')


# 5.判断老鼠是否可以从空隙中钻过
if gap>0.1:
    print("老鼠可以从空隙中钻过 ")
else:
    print("老鼠无法通过空隙")
    
    
