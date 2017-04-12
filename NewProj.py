#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Created by Sublime.
# User: Eric
# Date：2017年04月12日20:54:21
# Module：NewProj
from __future__ import unicode_literals
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys     
#from selenium.webdriver.common.keys import Keys#
from selenium.webdriver.support import select
#from selenium.webdriver.support.ui import Select#
from selenium.common import exceptions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest,time,re
import password
import randomName
#for child_of_root in root:
    #print child_of_root.tag, child_of_root.attrib


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
        driver.find_element_by_id("doLogin").click()
        # time.sleep(5)
        #driver.find_element_by_link_text(u"项目立项").click()
        driver.find_element_by_link_text("项目立项").click()
        #driver.find_element_by_xpath("//a[contains(@data-gh-route,'tal_start_project')]").click()
		#driver.find_element_by_xpath("//a[contains(.,' 项目立项')]").click()
        driver.find_element_by_id("addAsstes").click()
        driver.find_element_by_xpath("//input[@placeholder='请输入项目名称']").send_keys(randomName.generateName())
        driver.find_element_by_xpath("//select[@id='typeOid']").find_element_by_xpath("//select[@id='typeOid']//option[@data-extend='gpzc']").click()
        time.sleep(10)

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