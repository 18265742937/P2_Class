from selenium import webdriver

driver = webdriver.Firefox(executable_path = r"C:\Users\qq934\Desktop\geckodriver.exe")

url = "https://gp.qq.com/cp/a20190522gamedata/pc_list.shtml"

driver.get(url)













