
import random

print('欢迎来到猜数字游戏')
rr = random.randint(1, 100)
print('系统已生成1-100之间的数字。说出你心中的数字')
for i in range(1, 10000):

    s = input('请输入：')

    if not s.isdigit():
        print('输入错误，请重新输入')
        continue
    s = int(s)

    if s == rr:
        print('恭喜猜对了')
        print(f'一共猜了-->{i}')
        break
    elif s < rr:
        print('小了')
    else:
        print('大了')
