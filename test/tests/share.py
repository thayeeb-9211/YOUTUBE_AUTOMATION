#share button clicked then copy the link and close the dialog box
import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from subscribe import YoutubesubscribeTest

class YoutubeshareTest(unittest.TestCase):

    def __init__(self, email, password, phone_number):
        super().__init__()
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.driver = None


    def subscribing(self):
        # Initialize and run YoutubeSubscribeTest
        self.subscribed = YoutubesubscribeTest(self.email, self.password, self.phone_number)
        self.subscribed.run_test()
        self.driver = self.subscribed.driver
           
    def share(self):
        driver = self.driver
         
        # Locate and click the share button
        try:
            share_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="top-level-buttons-computed"]/yt-button-view-model/button-view-model'))
            )
            share_button.click()
            print("Share button clicked")
        except:
            print("Share button not found")

        time.sleep(10)

        # Wait for the share dialog to appear and copy the share link
        try:
            copy_link_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="copy-button"]/yt-button-shape/button'))
            )
            copy_link_button.click()
            print("Link copied")
        except:
            print("Copy link button not found")
        time.sleep(5)
        
        # click the close button on the share dialog
        try:
            copy_link_button.send_keys(Keys.ESCAPE)
            # close_button.click()
            print("Share dialog closed")
        except:
            pass
        time.sleep(10)
    
    def run_test(self):
        self.subscribing()
        self.share()

# Uncomment the below lines to test the subscribe button functionality independently
# if __name__ == "__main__":
#     email = 'yt.at.automation@gmail.com'
#     password = 'YoutubeAuto@123'
#     phone_number = '7338219832'
#     youtube_test = YoutubesubscribeTest(email, password, phone_number)
#     youtube_test.run_test()

