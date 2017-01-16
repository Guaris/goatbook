from selenium import webdriver
import unittest

class newVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    def tearDown(self):
        self.browser.quit()
    def test_can_start_a_list_and_retrieve_it_later(self):
        #new to-do app
        #go to check it homepage
        self.browser.get('http://localhost:8000')
        #she notice the page title and header mention to-do list
        self.assertIn('To-Do', self.browser.title)
        self.fail('finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
