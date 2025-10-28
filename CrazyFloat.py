#限制浮点数数位的三种核心方法
#第一种是通用格式化方法，通过调用format函数以格式化字符串控制小数位数，兼容性强。
a=float(input('输入第一个浮点数'))
b=float(input('输入第二个浮点数'))
print(a,'+',b,'=','{:.3f}'.format(a+b))
#第二种是控制显示，通过仅在输出时限制位数，不改变原数值，返回字符串格式，适合展示。
import math;
c=int(input('输入一个整数作为圆周率的限位点'))
print(f'{math.pi:.{c}}f')
#第三种
d=float(input('输入一个长长的浮点数'))
print(round(d,c))
