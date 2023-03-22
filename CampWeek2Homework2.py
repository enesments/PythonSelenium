from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Test_SauceWork:
     def test_empty_login(self):
         driver = webdriver.Chrome(ChromeDriverManager().install())
         driver.get("https://www.saucedemo.com/")
         sleep(5)
         usernameInput = driver.find_element(By.ID,"user-name")
         passworkInput = driver.find_element(By.ID,"password")
         sleep(2)
         usernameInput.send_keys("")
         passworkInput.send_keys("")
         sleep(2)
         loginBtn =driver.find_element(By.ID,"login-button")
         loginBtn.click()
         errrorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
         testResult = errrorMessage.text == "Epic sadface: Username is required"
         if (testResult==True):
             print("Username and password are required!!")
        
     def test_empty_password_login(self):
         driver = webdriver.Chrome(ChromeDriverManager().install())
         driver.get("https://www.saucedemo.com/")
         sleep(5)
         usernameInput = driver.find_element(By.ID,"user-name")
         passworkInput = driver.find_element(By.ID,"password")
         sleep(2)
         usernameInput.send_keys("1111")
         passworkInput.send_keys("")
         sleep(2)
         loginBtn =driver.find_element(By.ID,"login-button")
         loginBtn.click()
         errrorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
         testResult = errrorMessage.text == "Epic sadface: Password is required"
         if (testResult==True):
             print("Password is required!!") 
     def test_blocked_login(self):
         driver = webdriver.Chrome(ChromeDriverManager().install())
         driver.get("https://www.saucedemo.com/")
         sleep(5)
         usernameInput = driver.find_element(By.ID,"user-name")
         passworkInput = driver.find_element(By.ID,"password")
         sleep(2)
         usernameInput.send_keys("locked_out_user")
         passworkInput.send_keys("secret_sauce")
         sleep(2)
         loginBtn =driver.find_element(By.ID,"login-button")
         loginBtn.click()
         errrorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
         testResult = errrorMessage.text == "Epic sadface: Sorry, this user has been locked out."
         if (testResult==True):
             print("This User has been locked out !!")
     def test_empty_error_button(self):
         driver = webdriver.Chrome(ChromeDriverManager().install())
         driver.get("https://www.saucedemo.com/")
         sleep(5)
         usernameInput = driver.find_element(By.ID,"user-name")
         passworkInput = driver.find_element(By.ID,"password")
         sleep(2)
         usernameInput.send_keys("")
         passworkInput.send_keys("")
         sleep(2)
         loginBtn =driver.find_element(By.ID,"login-button")
         loginBtn.click()
         sleep(2)
         errorButtonIcon = driver.find_element(By.CLASS_NAME,"error-button")
         errorButtonIcon.click()
         print("Error button is closed!!")
         
     def test_standart_login(self):
         driver = webdriver.Chrome(ChromeDriverManager().install())
         driver.get("https://www.saucedemo.com/")
         sleep(5)
         usernameInput = driver.find_element(By.ID,"user-name")
         passworkInput = driver.find_element(By.ID,"password")
         sleep(2)
         usernameInput.send_keys("standard_user")
         passworkInput.send_keys("secret_sauce")
         sleep(2)
         loginBtn =driver.find_element(By.ID,"login-button")
         loginBtn.click()
         sleep(20)
         print("Succesfully login!!")
     def test_counter_login(self):
         driver = webdriver.Chrome(ChromeDriverManager().install())
         driver.get("https://www.saucedemo.com/")
         sleep(5)
         usernameInput = driver.find_element(By.ID,"user-name")
         passworkInput = driver.find_element(By.ID,"password")
         sleep(2)
         usernameInput.send_keys("standard_user")
         passworkInput.send_keys("secret_sauce")
         sleep(2)
         loginBtn =driver.find_element(By.ID,"login-button")
         loginBtn.click()
         sleep(10)
         products = driver.find_elements(By.CLASS_NAME,"inventory_item")
         print(f"This site has {len(products)} items !!")

         
        
testClass = Test_SauceWork()
#testClass.test_empty_login()
#testClass.test_empty_password_login()
#testClass.test_blocked_login()
#testClass.test_empty_error_button()
#testClass.test_standart_login()
testClass.test_counter_login()



while(True):
    continue
        
        
