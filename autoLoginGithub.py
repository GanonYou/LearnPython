from selenium import webdriver
import os,sys

#该脚本可以实现自动打开github主页，并用命令行参数提供的账号密码自动登录
browser = webdriver.Chrome('/Users/YWY/PythonProgram/chromedriver')
browser.get('https://github.com/login')

account = sys.argv[1]
password = sys.argv[2]

accountElem = browser.find_element_by_id('login_field')
accountElem.send_keys(account)
passwordElem = browser.find_element_by_id('password')
passwordElem.send_keys(password)
passwordElem.submit()
