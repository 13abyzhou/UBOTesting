#coding=utf-8
from selenium import webdriver
import csv
my_file='C:\\Python27\\Test_Case_UBO\\data\\userinfo.csv'
user=csv.reader(file(my_file,'rb'))

def fun():
    global un,pw
    for data in user:
       un,pw = data[0],data[1]
    return un,pw
#def fun(un=user[0], pw=user[1]):
#    return un, pw
#print un,pw
