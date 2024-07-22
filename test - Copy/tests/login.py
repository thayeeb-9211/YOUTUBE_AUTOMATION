import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class YouTubeLoginTest():
    def __init__(self, email, password, phone_number):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.email = email
        self.password = password
        self.phone_number = phone_number

    def login(self):
        driver = self.driver
        #Shows Homepage of youtube
        youtube = 'https://www.youtube.com/'
        
        # code for login test
        try:
            driver.get(youtube)
            time.sleep(5)
            # if not os.path.exists('screenshots'):
            #     os.makedirs('screenshots/login_page_test')
            # driver.save_screenshot('screenshots/login_page_test/homepage.png')

            WebDriverWait(driver, 20).until(EC.title_contains("YouTube"))


            sign_in_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@aria-label='Sign in']"))
            )
            sign_in_button.click()
            time.sleep(10)


            email_input = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@name='identifier' and @class='whsOnd zHQkBf']"))
            )
            email_input.send_keys(self.email)
            # if not os.path.exists('screenshots'):
            #     os.makedirs('screenshots/login_page_test')
            # driver.save_screenshot('screenshots/login_page_test/g-login-page.png')
            
            
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b']"))
            )
            next_button.click()


            password_input = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@name='Passwd' and @class='whsOnd zHQkBf']"))
            )
            password_input.send_keys(self.password)
            # if not os.path.exists('screenshots'):
            #     os.makedirs('screenshots/login_page_test')
            # driver.save_screenshot('screenshots/login_page_test/g-login-password-page.png')
            
            
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b']"))
            )
            next_button.click()
            time.sleep(15)


            if driver.current_url != youtube:
                try:
                    print("Checking whthere Recovery phone Page appeared or not.")
                    
                    try:
                        print("Finding the Confirm PHone div")
                        element = WebDriverWait(driver, 20).until(
                            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Confirm your recovery phone number')]"))
                        )
                        element.click()
                        print("Found the Confirm PHone div")
                    except :
                        print("Unable to find  the Confirm PHone div")
                    try:
                        print("Trying to click Dropdown menu")
                        dropdown_menu = WebDriverWait(driver, 20).until(
                            EC.element_to_be_clickable((By.XPATH, "//*[@id='countryList']/div/div[1]/div[2]"))
                        )
                        
                        dropdown_menu.click()
                        print("clicked Dropdown menu")
                    except :
                        print("Unable to click Dropdown menu")

                    try:
                        print("Trying to Select India from the list")
                        india_option = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, "//li[@data-value='in']"))
                        )
      
                        india_option.click()
                        print("India got successfully")
                    except :
                        print("India did'nt got")

                    try:
                        print("Trying to input number")
                        phone_input = WebDriverWait(driver, 10).until(
                            EC.visibility_of_element_located((By.XPATH, "//input[@type='tel']"))
                        )
                        phone_input.send_keys(self.phone_number)
                        print("Number input successfully")
                    except :
                        print("Unable to input Number")

                    try :
                        print("Finding Next button")
                        # Wait until the "Next" button is present in the DOM and visible
                        next_button = WebDriverWait(driver, 20).until(
                            EC.visibility_of_element_located((By.XPATH, "//*[text()='Next']"))
                        )

                        # Wait until the "Next" button is clickable
                        next_button = WebDriverWait(driver, 20).until(
                            EC.element_to_be_clickable((By.XPATH, "//*[text()='Next']"))
                        )
                        next_button.click()
                        print("Next button clicked successfuly")
                    except:
                        print("Next button not found or clicked.")
                    time.sleep(20)
                except Exception as e:
                    print(f"Error: {e}")
                    print("Recovery phone Page not appeared")

                try:
                    not_now_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[text()='Not now']"))
                    )
                    not_now_button.click()
                    time.sleep(20)
                except Exception as e:
                    print(f"Error: {e}")
                    print("Passkey Page not appeared")
                    
            print("Passkey Page not appeared")
            print("Login test is successfull without passkey page")
            return driver
        except Exception as e:
            print(f"Error: {e}")
            print("Unable to open YouTube")

# Uncomment the below lines to test the login independently
# if __name__ == "__main__":
    # email = 'Enter_your_Email_here'
    # password = 'Enter_your_Password_here'
    # phone_number = 'Enter_your_Phone_Number_here'
#     login = YouTubeLoginTest(email, password, phone_number)
#     login.login()