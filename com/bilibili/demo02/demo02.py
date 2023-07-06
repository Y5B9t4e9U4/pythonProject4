

for i in range(1, 4):
    user = input('请输入账号:')
    password = input('请输入密码:')  # 1.在输入账号密码的时候。按下回车的时候，进入if判断，如果成功break退出

    if user == 'admin' and password == '888':
        print('登录成功!')
        break  # 条件退出
    else:
        print('密码错误')  # 2.如果错误那就执行else，这个else只是提示代码
        if i < 3:
            print(f'剩余条件{3 - i}次机会')
else:
    print('今日登录已上线!')