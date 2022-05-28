#vpscrapy.py

#驱动地址
# http://npm.taobao.org/mirrors/chromedriver/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from contextlib import closing

import os

class SL:                              
    def __init__(self):
        # self.__bs=webdriver.Chrome(os.path.dirname(__file__)+'\chromedriver.exe')
        # self.__bs=webdriver.Chrome(os.path.dirname(__file__)+'\chromedriver.exe')
        self.__bs=webdriver.Firefox()
        self.__wait=WebDriverWait(self.__bs, 10)     #创建一个等待10秒的对象
        self.__options=webdriver.ChromeOptions()
        self.__options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')


    def get(self, url):
        self.__bs.get(url)
    
    def waitUntil(self, cssSelector):
        try:
            self.__wait.until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, cssSelector)))
            print("等待元素"+cssSelector)
        except:
            pass
    def pageSource(self):
        return self.__bs.page_source

    def findLinkByText(self, text):
        link = self.__bs.find_element_by_partial_link_text(text)
        print('找到"'+text+'"的url')
        return link
    
    def runScript(self, script, *args):
        print(args)
        self.__bs.execute_script('arguments[0].scrollIntoView();', *args)
