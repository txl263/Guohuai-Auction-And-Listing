#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Created by Sublime.
# User: Eric
# Date：2017年04月12日20:54:21
# Module：NewProj
from __future__ import unicode_literals
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys     
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest,time,re
import password
import randomName
import random
from datetime import datetime
from datetime import timedelta

#for child_of_root in root:
    #print child_of_root.tag, child_of_root.attrib
now = datetime.now()
delta=timedelta(minutes=5)  #时间间隔

name = randomName.generateName()    #项目名称
totalPrice = random.randint(100000, 999999999)  #资产总额
userName = 'qyqy'   #转让方用户编号
issuing = random.randint(100000000, 999999999)  #转让方机构
issuingCode = random.randint(100000000, 999999999)  #转让方机构代码
interestStartTime = (now - timedelta(days=10))  #存续期开始时间
interestEndTime = (now + timedelta(days=10))   #存续期结束时间
transferCount = str(random.randint(1000, 9999999))   #转让数量
listingStartTime = (now - timedelta(days=8)) #挂牌开始时间
listingEndTime = (now + delta)  #挂牌结束时间  必须大于挂牌开始时间7天以上
listingPrice = str(random.randint(10000, 999999))    #挂牌金额
transfereeStartTime = (listingEndTime + delta)  #资格审核开始时间
transfereeEndTime = (transfereeStartTime + delta)  #资格审核结束时间
qualifications = randomName.generateName()	#受让方资质
depositStartTime = (transfereeEndTime + delta)  #保证金缴纳开始时间
depositEndTime = (depositStartTime + delta)  #保证金缴纳结束时间
deposit = str(random.randint(10000, 99999999))   #保证金
auctionExpenses = str(random.randint(1000, 9999999)) #竞价费用
sellerTurnoverExpenses = str(random.randint(10000, 999999))  #卖方成交费用
buyerTurnoverExpenses =str(random.randint(10000, 99999999))     #买方成交费用
phone = randomName.generatePhone()  #发行商联系方式
address = randomName.generateString()   #发行商联系地址

print name
print "存续期开始时间：" + interestStartTime.strftime('%Y-%m-%d %H:%M:%S')
print "存续期结束时间：" + interestEndTime.strftime('%Y-%m-%d %H:%M:%S')
print "挂牌开始时间：" + listingStartTime.strftime('%Y-%m-%d %H:%M:%S')
print "挂怕结束时间：" + listingEndTime.strftime('%Y-%m-%d %H:%M:%S')
print "资格审核开始时间：" + transfereeStartTime.strftime('%Y-%m-%d %H:%M:%S')
print "资格审核结束时间：" + transfereeEndTime.strftime('%Y-%m-%d %H:%M:%S')
print "受让方资质：" + qualifications
print "保证金缴纳开始时间：" + depositStartTime.strftime('%Y-%m-%d %H:%M:%S')
print "保证金缴纳结束时间：" + depositEndTime.strftime('%Y-%m-%d %H:%M:%S')
print "保证金：" + deposit
print "竞价费用：" + auctionExpenses
print "卖方成交费用：" + sellerTurnoverExpenses
print "买方成交费用：" + buyerTurnoverExpenses
print "发行商联系方式：" + phone
print "发行商联系地址：" + address

#setUp 用于设置初始化的部分，在测试用例执行前，这个方法中的函数将先被调用。这里将浏览器的调用和URL的访问放到初始化部分。#
class NewProj(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.baseUrl = password.baseUrl
        self.verificationErrors=[]  #脚本运行时，错误的信息将被打印到这个列表中#
        self.accept_next_alert=True  #是否继续接受下一个警告#

    def test_NewProj(self):
        driver = self.driver
        driver.get(self.baseUrl)
        #driver.set_window_size(450, 800)
        driver.find_element_by_id("loginAccount").send_keys(password.loginAccount)
        driver.find_element_by_id("loginPassword").send_keys(password.loginPassword)
        time.sleep(0.5)
        driver.find_element_by_id("doLogin").click()
        # time.sleep(5)
        #driver.find_element_by_link_text(u"项目立项").click()
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,'addUser')))
        finally:
            driver.find_element_by_xpath("//span[contains(.,'金融资产转让')]").click()
        #driver.save_screenshot('screenshot.png')
        #driver.find_element_by_xpath("//a[contains(@data-gh-route,'tal_start_project')]").click()
		#driver.find_element_by_xpath("//a[contains(.,' 项目立项')]").click()
        locator = (By.LINK_TEXT,'项目立项')
        driver.find_element_by_link_text("项目立项").click()
        driver.find_element_by_id("addAsstes").click()
        driver.find_element_by_xpath("//input[@placeholder='请输入项目名称']").send_keys(name)
        #driver.find_element_by_xpath("//select[@id='typeOid']").find_element_by_xpath("//select[@id='typeOid']//option[@data-extend='gpzc']").click()
        Select(driver.find_element_by_xpath("//select[@id='typeOid']")).select_by_index(1)
        driver.find_element_by_xpath("//input[@placeholder='请输入资产总额']").send_keys(str(totalPrice))
        driver.find_element_by_xpath("//input[@placeholder='请输入转让方用户编号']").send_keys(userName)
        driver.find_element_by_xpath("//input[@placeholder='请输入转让方机构']").send_keys(str(issuing))
        driver.find_element_by_xpath("//input[@placeholder='请输入转让方机构代码']").send_keys(issuingCode)
        #driver.find_element_by_xpath("//input[@placeholder='请输入存续期开始时间']").clear
        driver.find_element_by_xpath("//input[@placeholder='请输入存续期开始时间']").click()
        driver.find_element_by_xpath("//input[@placeholder='请输入存续期开始时间']").clear()
        driver.find_element_by_xpath("//input[@placeholder='请输入存续期开始时间']").send_keys(interestStartTime.strftime('%Y-%m-%d %H:%M:%S'))

        driver.find_element_by_xpath("//input[@placeholder='请输入存续期结束时间']").click()
        driver.find_element_by_xpath("//input[@placeholder='请输入存续期结束时间']").clear()
        driver.find_element_by_xpath("//input[@placeholder='请输入存续期结束时间']").send_keys(interestEndTime.strftime('%Y-%m-%d %H:%M:%S'))

        driver.find_element_by_xpath("//input[@placeholder='请输入转让数量']").send_keys(str(transferCount))

        driver.find_element_by_xpath("//input[@placeholder='请输入挂牌开始时间']").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//input[@placeholder='请输入挂牌开始时间']").send_keys(Keys.CONTROL ,'a')
        driver.find_element_by_xpath("//input[@placeholder='请输入挂牌开始时间']").clear()
        driver.find_element_by_xpath("//input[@placeholder='请输入挂牌开始时间']").send_keys(listingStartTime.strftime('%Y-%m-%d %H:%M:%S'))

        driver.find_element_by_xpath("//input[@placeholder='请输入挂牌结束时间']").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//input[@placeholder='请输入挂牌结束时间']").send_keys(Keys.CONTROL ,'a')
        driver.find_element_by_xpath("//input[@placeholder='请输入挂牌结束时间']").clear()
        driver.find_element_by_xpath("//input[@placeholder='请输入挂牌结束时间']").send_keys(listingEndTime.strftime('%Y-%m-%d %H:%M:%S'))

        driver.find_element_by_xpath("//input[@placeholder='请输入挂牌金额(元)']").send_keys(str(listingPrice))
        
        driver.find_element_by_xpath("//input[@placeholder='请输入资格审核开始时间']").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//input[@placeholder='请输入资格审核开始时间']").send_keys(Keys.CONTROL ,'a')
        driver.find_element_by_xpath("//input[@placeholder='请输入资格审核开始时间']").clear()
        driver.find_element_by_xpath("//input[@placeholder='请输入资格审核开始时间']").send_keys(transfereeStartTime.strftime('%Y-%m-%d %H:%M:%S'))

        driver.find_element_by_xpath("//input[@placeholder='请输入资格审核结束时间']").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//input[@placeholder='请输入资格审核结束时间']").send_keys(Keys.CONTROL ,'a')
        driver.find_element_by_xpath("//input[@placeholder='请输入资格审核结束时间']").clear()
        driver.find_element_by_xpath("//input[@placeholder='请输入资格审核结束时间']").send_keys(transfereeEndTime.strftime('%Y-%m-%d %H:%M:%S'))

        driver.find_element_by_xpath("//input[@placeholder='请输入受让方资质']").send_keys(qualifications)

        driver.find_element_by_xpath("//input[@placeholder='请输入保证金缴纳开始时间']").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//input[@placeholder='请输入保证金缴纳开始时间']").send_keys(Keys.CONTROL ,'a')
        driver.find_element_by_xpath("//input[@placeholder='请输入保证金缴纳开始时间']").clear()
        driver.find_element_by_xpath("//input[@placeholder='请输入保证金缴纳开始时间']").send_keys(depositStartTime.strftime('%Y-%m-%d %H:%M:%S'))

        driver.find_element_by_xpath("//input[@placeholder='请输入保证金缴纳结束时间']").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//input[@placeholder='请输入保证金缴纳结束时间']").send_keys(Keys.CONTROL ,'a')
        driver.find_element_by_xpath("//input[@placeholder='请输入保证金缴纳结束时间']").clear()
        driver.find_element_by_xpath("//input[@placeholder='请输入保证金缴纳结束时间']").send_keys(depositEndTime.strftime('%Y-%m-%d %H:%M:%S'))

        driver.find_element_by_xpath("//input[@placeholder='请输入保证金']").send_keys(deposit)
        driver.find_element_by_xpath("//input[@placeholder='请输入竞价费用']").send_keys(auctionExpenses)
        driver.find_element_by_xpath("//input[@placeholder='请输入卖方成交费用']").send_keys(sellerTurnoverExpenses)
        driver.find_element_by_xpath("//input[@placeholder='请输入买方成交费用']").send_keys(buyerTurnoverExpenses)
        driver.find_element_by_xpath("//input[@placeholder='请输入电话号码']").send_keys(phone)
        driver.find_element_by_xpath("//input[@placeholder='请输入发行商联系地址']").send_keys("等待替换")

        driver.find_element_by_id("assetsDesc").click()
        driver.find_element_by_id("assetsDesc").clear()
        driver.find_element_by_id("assetsDesc").send_keys(u"资产描述")
        driver.find_element_by_id("remark").click()
        driver.find_element_by_id("remark").clear()
        driver.find_element_by_id("remark").send_keys("备注")
        driver.find_element_by_name("yupUpload").clear()
        driver.find_element_by_name("yupUpload").send_keys("C:\\Users\\Eric\\Desktop\\ride.bat")
        driver.execute_script("var q=document.documentElement.scrollTop=10000")

        submitOrSave = random.randint(0, 1)
        if submitOrSave == 0:
            btn = "submitBtn"
        else:
            btn = ("saveBtn")
        

        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,btn)))
        finally:
            driver.find_element_by_id(btn).click()

        time.sleep(100)



    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    def tearDown(self):
        #self.driver.quit()
        self.assertEqual([],self.verificationErrors)
        '''
        tearDown 方法在每个测试方法执行后调用，这个地方做所有清理工作，如退出浏览器等。 
        self.assertEqual([], self.verificationErrors) 是个难点，
        对前面verificationErrors方法获得的列表进行比较；如查verificationErrors的列表不为空，输出列表中的报错信息。'''
if __name__=="__main__":
    unittest.main() #执行用例#
#suite = unittest.TestLoader().loadTestsFromTestCase(Wukong)
#unittest.TextTestRunner(verbosity=2).run(suite)