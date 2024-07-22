import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from like_dislike import YoutubelikedislikeTest #import like_dislike class

class YoutubesubscribeTest(unittest.TestCase):

    def __init__(self, email, password, phone_number):
        super().__init__()
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.driver = None

    def likes_dislikes(self):
        # Initialize and run YoutubelikesdislikesTest
        self.L_D_instance = YoutubelikedislikeTest(self.email, self.password, self.phone_number)
        self.L_D_instance.run_test()
        self.driver = self.L_D_instance.driver
        
    def subscribe(self):
        driver = self.driver

        # Locate and click the subscribe button
        try:
            subscribe_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="subscribe-button"]/ytd-subscribe-button-renderer'))
            )
            subscribe_button.click()
            print("Subscribed to the channel")
        except:
            print("Subscribe button not found")
        time.sleep(10)
    
    def run_test(self):
        self.likes_dislikes()
        self.subscribe()

# Uncomment the below lines to test the subscribe button functionality independently
# if __name__ == "__main__":
#     email = 'yt.at.automation@gmail.com'
#     password = 'YoutubeAuto@123'
#     phone_number = '7338219832'
#     youtube_test = YoutubesubscribeTest(email, password, phone_number)
#     youtube_test.run_test()