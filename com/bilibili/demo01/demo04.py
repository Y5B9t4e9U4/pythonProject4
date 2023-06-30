# 1.导入随机包
import random

# 定义列表
choices = ['石头', '剪刀', '布']
computer_choice = random.choice(choices)  # choice是一个random中的方法。用于可迭代对象中的元素并返回

# 用户输入
user_choice = input('请输入你的选择(石头,剪刀,布):')

print('电脑选择:', computer_choice)
print('用户选择:', user_choice)

if user_choice in choices:
    if user_choice == computer_choice:
        print('平局')
    elif (
            (user_choice == '石头' and computer_choice == '剪刀')
            or (user_choice == '剪刀' and computer_choice == '布')
            or (user_choice == '布' and computer_choice == '石头')
    ):
        print('你赢了?')
    else:
        print('你输了?')
else:
    print('无效选择!')
