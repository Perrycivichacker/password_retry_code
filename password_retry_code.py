password = 'a123456'
retry_time = 3
while retry_time != 0:
	code = input('請輸入密碼: ')
	if code != password:
		retry_time = retry_time - 1
		print('密碼錯誤，還有', retry_time, '次機會')
	else:
		print('登入成功')
		break