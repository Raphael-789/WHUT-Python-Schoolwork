#计算到午夜时间，三维转换一维


hour = int(input())
minute = int(input())
second = int(input())
print(f'{hour:02}:{minute:02}:{second:02}')
total_seconds = 86400
used_seconds = hour*3600+minute*60+second
remaining_seconds = total_seconds - used_seconds
print(f'距离午夜还剩余{remaining_seconds}秒')
