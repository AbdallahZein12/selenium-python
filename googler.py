from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
 
chrome_path = r"C:\Users\abdal\Downloads\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.minimize_window()
def searcher1():
    driver.get("https://www.google.com")
    search = input("Search> ")
    searcher = driver.find_element("xpath","""/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input""")
    searcher.send_keys(search)
    searcher.send_keys(Keys.ENTER)
    posts = driver.find_elements(By.CLASS_NAME, "VwiC3b")
    for post in posts:
        print("\033[32m", post.text, "\n")
    
    while True:
        print("\033[0m")
        again = input("search again?(y/n)> ")
        if again == "y" or again == "Y":
            searcher1()
        elif again == "n" or again == "N":
            print("\033[0m")
            break
        else:
            print("\033[31m","Please try again!","\033[0m")
            continue
                
    exit()
    


    
searcher1()
