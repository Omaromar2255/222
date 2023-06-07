import time
from selenium import webdriver
import csv
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager

# تحديد مسار ملف تهيئة متصفح Chrome

driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')

# فتح صفحة واتساب وتسجيل الدخول
driver.get('https://web.whatsapp.com')
input('قم بتسجيل الدخول من المتصفح، ثم اضغط Enter للمتواصل العمل...')
time.sleep(5)

# فتح قائمة الخيارات واختيار "إضافة مشارك"
options_button = driver.find_element(By.XPATH, '//*[@id="main"]/header/div[2]/div[2]/span')
options_button.click()
time.sleep(5)
add_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[6]/span/div/span/div/div/div/section/div[6]/div[2]/div[1]/div[2]/div/div')
add_button.click()
time.sleep(5)

# افتح ملف النص واقرأ كل سطر وأضف الرقم إلى مجموعة الأعضاء
with open('members.txt', 'r') as f:
    members = [line.strip() for line in f.readlines()]


# إضافة كل عضو إلى المجموعة
for group_name in members:
    search_box = driver.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p')
    search_box.clear()
    search_box.send_keys(group_name)
    time.sleep(1)
    group = driver.find_element(By.XPATH, '//span[@title="'+group_name+'"]')
    group.click()
    time.sleep(1)
    clar = driver.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div[1]/div/div/span/button/span')
    clar.click()
    time.sleep(1)
    
# انتظر حتى يتم تسجيل الدخول يدويًا إلى موقع واتساب ويب
input('يرجى تسجيل الدخول إلى واتساب ويب والضغط على مفتاح Enter للمتابعة...')
add = driver.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/span[2]/div/div/div/span')
add.click()
time.sleep(3)
www = driver.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/button[2]/div/div')
www.click()
time.sleep(12)
input('يرجى تسجيل الدخول إلى واتساب ويب والضغط على مفتاح Enter للمتابعة...')

# إغلاق المتصفح عند الانتهاء من إضافة الأعضاء إلى المجمووعودة الى البرنامج الرئيسي
driver.quit()




