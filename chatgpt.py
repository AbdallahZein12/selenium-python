import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
chrome_options = Options()


chrome_path = r"C:\Users\abdal\Downloads\chromedriver.exe"
chrome_options.headless = True
driver = uc.Chrome(options=chrome_options)




driver.get("https://chat.openai.com/auth/login")
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """/html/body/div/div/div/div[4]/button[1]""")))
driver.find_element("xpath","""/html/body/div/div/div/div[4]/button[1]""").click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """/html/body/main/section/div/div/div/div[3]/form[1]/button""")))
driver.find_element(By.XPATH,"""/html/body/main/section/div/div/div/div[3]/form[1]/button""").click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(("id", """identifierId""")))
print("\033[33m")
email = input("email> ")
print("\033[33m")
email1 = driver.find_element("id","""identifierId""").send_keys(email)
driver.find_element("xpath","""//*[@id="identifierNext"]/div/button/span""").click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """//*[@id="password"]/div[1]/div/div[1]/input""")))
passw = input("password> ")
print()
password = driver.find_element("xpath","""//*[@id="password"]/div[1]/div/div[1]/input""").send_keys(passw)
driver.find_element("xpath","""//*[@id="passwordNext"]/div/button/span""").click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button""")))
driver.find_element("xpath","""//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button""").click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]""")))
driver.find_element("xpath","""//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]""").click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]""")))
driver.find_element("xpath","""//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]""").click()




searcher = driver.find_element("xpath","""//*[@id="__next"]/div/div/main/div[2]/form/div/div[2]/textarea""")
searcher.send_keys("Hi")
searcher.send_keys(Keys.ENTER)
posts = driver.find_elements(By.CLASS_NAME,"""markdown""")[-1]
time.sleep(7)
print("\033[32m", posts.text, "\033[0m")
def searcher1():
        print()
        search = input("input> ")
        print()
        searcher.send_keys(search)
        searcher.send_keys(Keys.ENTER)
        posts = driver.find_elements(By.CLASS_NAME,"""markdown""")[-1]
        time.sleep(13)
        print("\033[32m",posts.text,end="\n")
        while True:
                print("\033[0m")
                again = input("search again?(y/n)> ")
                if again == "y" or again == "Y":
                        searcher1()
                elif again == "n" or again == "N":
                        break
                else:
                        print("\033[31m","Please try again!","\033[0m")
                        continue

        exit()
searcher1()
