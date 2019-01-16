#coding=utf-8

from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
class NewVisitorTest(unittest.TestCase):

    def  setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
#小花听说有一个待办事项的网站很好
#她去看了这个应用的首页
        self.browser.get("http://localhost:8000")
#她注意到这个首页的标题和头部包含“To-Do”
        self.assertIn("To-Do",self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)
#应用邀请她输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute("placeholder"),
            'Enter a to-do item'
        )
#她在文本框输入了"Buy  woolen yarn " (购买毛线)
#她的爱好是织毛衣
        inputbox.send_keys("Buy woolen yarn")

#按回车键页面更新了
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
# 待办事项中显示“1：Buy woolen yarn”
        table = self.browser.find_element_by_id('id_list_table')
        rows  = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text=="1:Buy woolen yarn"for row in rows),
                "new to do item did not apper in table"
        )
#页面中又显示了一个文本框，可以输入其他待办事项
#她输入了"Knit a sweater with wool”(使用毛线织毛衣)
        self.fail("Finish the test")
#页面再次跟新，他的清单中显示了这两个待办事项
#[..]
if __name__=='__main__':
      unittest.main()