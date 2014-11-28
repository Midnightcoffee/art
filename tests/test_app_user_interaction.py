#!/usr/local/bin/python
import unittest
import sys
from selenium import webdriver

servers = {
        'live' : 'http://safe-sands-8472.herokuapp.com/',
        'local': 'http://127.0.0.1:5000/'
        }

class TestApp(unittest.TestCase):


    BASE = servers['local']

    @classmethod
    def setUpClass(cls):
        cls.c = webdriver.PhantomJS()

    def setUp(self):
        self.c.get(self.BASE)

    def tearDown(self):
        self.c.quit()

    def test_app(self):
        #test layout
        self.assertEqual("DREW'S ART", self.c.find_element_by_class_name('logo').text)
        self.assertTrue('about' in self.c.find_element_by_tag_name('nav').text.lower())
        self.assertTrue('about' in self.c.find_element_by_id('fnav').text.lower())
        self.assertEqual(3, len(self.c.find_elements_by_class_name('cover_art')))
        self.assertEqual(4, len(self.c.find_elements_by_tag_name('meta')))
        self.assertTrue('NY' in self.c.find_element_by_class_name('copy_right'))

        #test index
        self.assertEqual('Home', self.c.title)
        self.assertEqual(3, len(self.c.find_elements_by_class_name('cover_art')))
        

        

if __name__ == '__main__':
    if len(sys.argv) > 1: TestApp.BASE = servers[sys.argv.pop()]
    unittest.main()

