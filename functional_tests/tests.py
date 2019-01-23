#coding=utf-8

from selenium import webdriver
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
MAX_WAIT = 10
import time
class NewVisitorTest(LiveServerTestCase):

    def  setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
    def wait_for_row_in_list_table(self,row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id("id_list_table")
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(
                    row_text ,[row.text for row in rows]
                )
                return
            except(AssertionError,WebDriverException) as e:
                if time.time()-start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
    def test_can_start_a_list_and_retrieve_it_later(self):
#小花听说有一个待办事项的网站很好
#她去看了这个应用的首页
        self.browser.get(self.live_server_url)
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
#按回车键页面更新了
        inputbox.send_keys("Buy woolen yarn")
        inputbox.send_keys(Keys.ENTER)
# 待办事项中显示“1：Buy woolen yarn”
        self.wait_for_row_in_list_table( "1:Buy woolen yarn")
#页面中又显示了一个文本框，可以输入其他待办事项
#她输入了"Knit a sweater with wool”(使用毛线织m毛衣)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("Knit a sweater with wool")
        inputbox.send_keys(Keys.ENTER)
#页面再次跟新，他的清单中显示了这两个待办事项
# 待办事项中显示  1：Buy woolen yarn
#                 2:Knit a sweater with wool
        self.wait_for_row_in_list_table( "1:Buy woolen yarn")
        self.wait_for_row_in_list_table( "2:Knit a sweater with wool")
        self.fail("Finish the test")

#[..]
