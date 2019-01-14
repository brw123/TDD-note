#coding=utf-8

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
        def  setUp(self):
               self.browser = webdriver.Firefox()
        def tearDown(self):
               self.browser.quit()

        def test_can_start_a_list(self):
#老王听说有一个待办事项的网站很好
#他去看了这个应用的首页
               self.browser.get("http://localhost:8000")
#他注意到这个首页的标题和头部包含“To-Do”
               self.assertIn("To-Do",self.browser.title)
               self.fail("Finish the test")
#应用邀请他输入一个待办事项
#接下来写的跟上一个test.py 一样的故事

if __name__=='__main__':
      unittest.main()