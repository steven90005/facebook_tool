# -*- coding: utf-8 -*- 

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
 
# available since 2.4.0
from selenium.webdriver.support.ui import WebDriverWait
 
# available since 2.26.0
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
import time

# 建立 driver
#關閉chrom跳出通知  
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
#driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='C:\\Users\\sylu\\Desktop\\py\chromedriver.exe')

# 需下載 Browser Drivers http://www.seleniumhq.org/download/ 
# 若 geckodriver 有在 PATH 中， firefox 可不帶路徑參數
#driver = webdriver.Chrome('chromedriver.exe') 

# 去 google
driver.get("https://www.facebook.com/login.php")

 
# 顯示標題
print(driver.title)

inputControl = driver.find_element_by_name("email")
inputControl.send_keys("mail")
inputControl = driver.find_element_by_name("pass") 
inputControl.send_keys("pass")
inputControl.submit()

#driver.implicitly_wait(10)
#driver.maximize_window()
driver.get("https://www.facebook.com/profile")


length=5000 
for i in range(0,5): 
    js="var q=document.documentElement.scrollTop="+str(length)
    print(js)
    driver.execute_script(js)  
    time.sleep(1) 
    length+=50000 


    
driver.implicitly_wait(10)

private_btn = driver.find_elements_by_css_selector("._6a._43_1._4f-9._nws._21o_._fol")
print(private_btn)


listlen=len(private_btn)
print(listlen)


js = "var q=document.documentElement.scrollTop=0"  
driver.execute_script(js)  
for i in range(0,listlen):
#for i in range(listlen)[::-1]:  
    print()  
    print("private_btn:"+str(private_btn[i]))
    ActionChains(driver).move_to_element(private_btn[i]).click(private_btn[i]).perform() 

    driver.implicitly_wait(20)

print("----------------------------------------------")  

click_globle = driver.find_elements_by_css_selector("._54ni._4h7j._k_c._k_e._2930")
print("["+str(len(click_globle))+"] click_globle:"+str(click_globle))
js = "var q=document.documentElement.scrollTop=0"  
driver.execute_script(js)  
for i in range(0,listlen-1):
    print("now "+str(i))  
    print("private_btn:"+str(private_btn[i]))
    ActionChains(driver).move_to_element(private_btn[i]).click(private_btn[i]).perform() 

    driver.implicitly_wait(3)
    
    ActionChains(driver).move_to_element(click_globle[i]).click(click_globle[i]).perform()

    driver.implicitly_wait(5)
    time.sleep(3)


try:
    ActionChains(driver).move_to_element(private_btn[listlen-1]).click(private_btn[listlen-1]).perform() 
    driver.implicitly_wait(3)
    ActionChains(driver).move_to_element(click_globle[listlen-1]).click(click_globle[listlen-1]).perform()
    time.sleep(3)
except:
    print("don't mind")


driver.quit()


