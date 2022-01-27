import sys
import random
from selenium import webdriver
import unittest

import util

class Test(unittest.TestCase):
    """ Demonstration: Get Chrome to generate fullscreen screenshot """

    def setUp(self):
        # setup disguised chrome browser.
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.chrome_options.add_experimental_option('useAutomationExtension', False)
        self.chrome_options.add_argument('lang=zh-CN,zh,zh-TW,en-US,en')
        self.chrome_options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) '
            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')
        self.chrome_options.add_argument("disable-blink-features=AutomationControlled")
        self.driver = webdriver.Chrome("./chromedriver", chrome_options=self.chrome_options)
        self.driver.get("https://douban.com/")

    def tearDown(self):
        self.driver.quit()

    def test_fullpage_screenshot(self):
        ''' Generate document-height screenshot '''
        #url = "http://effbot.org/imagingbook/introduction.htm"
        ori_url = input("input url: ")
        url_list = self.generate_urls(ori_url)
        for i in range(len(url_list)):
            self.driver.get(url_list[i])
            util.fullpage_screenshot(self.driver, str(i).zfill(5)+".png")

    def generate_urls(self, ori_url):
        url_list = []
        for i in range(1, 247):
            url_list.append(ori_url+'?p='+str(i))
        print(url_list)
        return url_list


if __name__ == "__main__":

    unittest.main(argv=[sys.argv[0]])


