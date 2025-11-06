python=3
math=4
english=4
pe=2
military=2
philosophy=2
total_credits=python+math+english+pe+military+philosophy
tuition_per_credit=eval (input ('请输入每学分学费金额：'))
monthly_living=eval (input ('请输入你每个月生活费：'))
#eval()接受任何合法Python表达式字符串，如'1+2''a*3'。灵活性极强。
#但因此可能被破坏
#核心优势；变量引用场景、表达式计算场景、类型转换如int-float
total_tuition=total_credits*tuition_per_credit
total_living=monthly_living*5
total_cost=total_tuition+total_living
loan_amount=total_cost*0.6
print (f'本学期你能够贷款{loan_amount:.2f}元')
