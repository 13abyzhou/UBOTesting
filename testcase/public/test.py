#coding:utf-8
import codecs

fp=open('C:\\Python27\\Test_Case_UBO\\data\\test.txt','rb')
users=[]
pwds=[]
lines=fp.readlines()
def fun():
    for data in lines:
        name,pwd=data.split(',')
        name=name.strip('\t\r\n')
        pwd=pwd.strip('\t\r\n')
        users.append(name)
        pwds.append(pwd)
        print "user:%s(len(%d))" %(name,len(name))
        print "pwd:%s(len(%d))" %(pwd,len(pwd))
#        return name,pwd
    fp.close()
