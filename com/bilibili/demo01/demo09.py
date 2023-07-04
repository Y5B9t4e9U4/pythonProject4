

for i in range(1, 4):
    input_user = input('请输入用户名：')
    input_pass = input('请输入密码：')
    if input_user == 'admin' and input_pass == '888':
        print('输入正确!')
        break
    else:
        print('密码错误')
        if i < 3:
            print(f'还有{3 - i}次机会')
else:
    print('今日已上线')