from django.template.loader import render_to_string
from django.urls import resolve
from django.test import TestCase
from  lists.views import  home_page
from  django.http import  HttpRequest


class HomePageTest(TestCase):
#这个方法是检查“/” 能否映射到 home_page 函数
    def test_url_resolve_to_home_page_view(self):
        found = resolve("/")
        # resolve 用于解析URl ,并映射到相应的视图函数。
        self.assertEqual(found.func, home_page)

#视图函数的测试
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf-8')
        self.assertTrue(html.strip().startswith('<html>'))
        self.assertIn("<title>To-Do list</title>",html)
        self.assertTrue(html.endswith('</html>'))


