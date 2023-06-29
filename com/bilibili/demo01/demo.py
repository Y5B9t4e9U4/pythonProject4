
import random

print('今日竞猜商品为小米扫地机器人!价格在[1000-1500之间]')
rd = random.randint(1000, 1500)
print('系统已生成随机数,请竞猜')

while True:

    try:
        rr = int(input('请输入竞猜数字(1000/1500):'))

        if rr == rd:
            print('恭喜你，获得机器人!')
            break
        elif rr < rd:
            print('小了')
        else:
            print('大了')
    except Exception as e:
        print('error info:', e)


