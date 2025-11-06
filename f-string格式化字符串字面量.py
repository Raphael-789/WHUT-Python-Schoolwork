python = 3
math = 4
english = 4
pe = 2
military = 2
philosophy = 2
total_credits = python + math + english + pe + military + philosophy
tuition_per_credit = int(input())
total_tuition = total_credits * tuition_per_credit
print(f'你本学期选修了{total_credits}个学分。')
print(f'你应缴纳的学费为{total_tuition}元。')
#f是f-string的缩写，全称formatted string literal
#(格式化字符串字面量也即常量，和变量对应)
#能直接嵌入变量f'a = {a+b}'，让字符串拼接更简洁直接
#变量存储引用数据，字面量写出固定值
