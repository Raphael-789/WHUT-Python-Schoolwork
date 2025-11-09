# 一
# 直接定义定义月份与缩写的映射字典
# month_abbr_map：变量名，用于存储 “月份单词” 和 “对应缩写” 的映射关系，命名体现 “月份（month）- 缩写（abbr）- 映射（map）” 的含义。
# {}：字典的语法符号，内部存储键值对（key: value）。
# 每个 '单词': '缩写' 是一组键值对：
# 键（key）：如 'january'，是小写的月份英文单词，用于匹配用户输入（用户输入会转为小写）。
# :：键值对的分隔符，左边是键，右边是值。
# 值（value）：如 'Jan.'，是该月份对应的标准缩写，直接作为正确结果输出。
# ,：用于分隔不同的键值对（最后一组可省略）。

month_abbr_map = {
    'january': 'Jan.',
    'february': 'Feb.',
    'march': 'Mar.',
    'april': 'Apr.',
    'may': 'May.',
    'june': 'Jun.',
    'july': 'Jul.',
    'august': 'Aug.',
    'september': 'Sept.',
    'october': 'Oct.',
    'november': 'Nov.',
    'december': 'Dec.'
}


# 二
# 读取输入并转换为小写（去除首尾空格，避免意外空格导致的错误）
# .strip()：字符串方法，用于去除输入内容首尾的空白字符（如空格、换行符），避免用户误输入空格导致匹配失败。
# .lower()：字符串方法，将输入的所有字母转为小写，确保无论用户输入大小写（如 AuGuSt），都能统一与字典中小写的键（如 'august'）匹配。

user_input = input().strip().lower()


# 三
# 直接通过字典查找结果（O(1)复杂度，比列表遍历更高效）
# month_abbr_map.get(...)：字典的 get 方法，用于根据键查找对应的值。
# 第一个参数 user_input：要查找的键（即处理后的用户输入）。
# 第二个参数 "spelling mistake"：当键不存在时的默认返回值（即输入拼写错误时的提示）。
# 整体逻辑：如果用户输入（处理后）在字典的键中存在，则返回对应的缩写并打印；否则返回 “spelling mistake” 并打印。

print(month_abbr_map.get(user_input, "spelling mistake"))
