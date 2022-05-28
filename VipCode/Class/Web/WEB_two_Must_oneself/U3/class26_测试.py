from selenium import webdriver

url = "https://gp.qq.com/cp/a20190522gamedata/pc_list.shtml"
driver = webdriver.Firefox()
driver.get(url)

driver.waitUn