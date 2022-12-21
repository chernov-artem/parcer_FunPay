''' парсит цены с FunPay'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

options = webdriver.ChromeOptions()

#disablw webdriver mode
options.add_argument("--disable-blink-features=AutomationControlled")




# user agent
my_user_agent = "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)"
options.add_argument(f"user-agent={my_user_agent}")
driver = webdriver.Chrome(executable_path='Chrom/chromedriver.exe', options=options)

url = "https://funpay.com/chips/6/"

def aion_ruof(serv):
    driver.get("https://funpay.com/chips/6/")
    driver.implicitly_wait(5)
    # выбираем сервер

    select_serv = Select(driver.find_element(By.XPATH,
                                             "//*[@id='content']/div/div[3]/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div[1]/div/form/div[1]/select"))
    select_serv.select_by_visible_text(serv)
    # #выбираем расу
    select_race = Select(driver.find_element(By.XPATH,
                                             "//*[@id='content']/div/div[3]/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div[1]/div/form/div[2]/select"))
    select_race.select_by_visible_text("Элийцы")

def sellers():

    seller_list = driver.find_elements(By.CLASS_NAME, "tc-item")
    user_list = []
    for i in seller_list:
        # seller_name = i.find_element(By.CLASS_NAME, "media-user-name").find_element("span").text
        user = i.find_element(By.CLASS_NAME, "media-user-name").text
        amound = i.find_element(By.CLASS_NAME, "tc-amount").text
        price = i.find_element(By.CLASS_NAME, "tc-price").text
        user_list.append([user, amound, price])
        # print(user,"    ", amound, "    ", price)

    for i in range(2, 7):
        print(user_list[i])



try:
    # aion_ruof("Асгард")
    # sellers()
    # driver.implicitly_wait(5)
    aion_ruof("Сиэль")
    sellers()
    # driver.get(url)
    # driver.implicitly_wait(5)
    # #выбираем сервер
    #
    # select_serv = Select(driver.find_element(By.XPATH, "//*[@id='content']/div/div[3]/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div[1]/div/form/div[1]/select"))
    # select_serv.select_by_visible_text("Асгард")
    # # #выбираем расу
    # select_race = Select(driver.find_element(By.XPATH, "//*[@id='content']/div/div[3]/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div[1]/div/form/div[2]/select"))
    # select_race.select_by_visible_text("Элийцы")
    #
    # seller_list = driver.find_elements(By.CLASS_NAME, "tc-item")
    # user_list = []
    # for i in seller_list:
    #     # seller_name = i.find_element(By.CLASS_NAME, "media-user-name").find_element("span").text
    #     user = i.find_element(By.CLASS_NAME, "media-user-name").text
    #     amound = i.find_element(By.CLASS_NAME, "tc-amount").text
    #     price = i.find_element(By.CLASS_NAME, "tc-price").text
    #     user_list.append([user, amound, price])
    #     # print(user,"    ", amound, "    ", price)
    #
    # for i in range(2, 7):
    #     print(user_list[i])


    time.sleep(999)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()