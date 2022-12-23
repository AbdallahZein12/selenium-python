#Web scraping script that takes a user's input, googles it and prints descriptions of top results!, User is allowed multiple inputs respectively.


#importing presents, the chrome web driver, the Keys library to press keys, and the "By" library to select elements by class name. 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
 
chrome_path = r"C:\Users\abdal\Downloads\chromedriver.exe"
chrome_options.headless = True
driver = webdriver.Chrome(options=chrome_options)

def searcher1(): #subroutine to allow for the user to repeat actions depending on later inputs 
    driver.get("https://www.google.com") 
    search = input("Search> ")
    searcher = driver.find_element("xpath","""/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input""") #locate the search bar and define it under "searcher"
    searcher.send_keys(search) #input the user's input from 'search'
    searcher.send_keys(Keys.ENTER) #press enter
    posts = driver.find_elements(By.CLASS_NAME, "VwiC3b") #locate web descriptions using their class names
    for post in posts:
        print("\033[32m", post.text, "\n") #print each of them respectively, colored green and each seperated by a line
    
    while True:
        print("\033[0m")
        again = input("search again?(y/n)> ") #asking for repetition in a loop to ensure wrong inputs are given second chances with a try again input 
        if again == "y" or again == "Y":
            searcher1() #goes back to the subroutine
        elif again == "n" or again == "N":
            print("\033[0m")
            break #breaks and exits the program
        else:
            print("\033[31m","Please try again!","\033[0m")
            continue # prints error message and requests a reinput 
                
    exit()
    


    
searcher1()
