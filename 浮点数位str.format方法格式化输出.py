ab = 0
cd = 1
ab = float(input())
cd = float(input())
ad = ab/2
radius = (ad**2+cd**2)/(2*cd)
print(f"{radius:.2f}")
#冒号为格式说明符的分隔标记。
#点号为小数精确位的固定语法，点n表示后接n位。
#f表示格式化的是浮点数。
#radius:.2f读作直径格式化为二位浮点数。
