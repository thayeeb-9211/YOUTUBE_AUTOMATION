import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from search import YoutubeSearchTest


class YoutubeSkipTest(unittest.TestCase):

    def __init__(self, email, password, phone_number):
        super().__init__()
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.driver = None

    def searches(self):
        # Initialize and run YoutubeSearchTest
        self.log_search = YoutubeSearchTest(self.email, self.password, self.phone_number)
        self.log_search.run_test()
        self.driver = self.log_search.driver
        
    def skip_ad(self):
        driver = self.driver
        # Wait for the ad to load (if any)
        try:
            ad_loaded = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//button[@id="skip-button:3"]'))
            )
            # Skip the ad
            ad_loaded.click()
            print("Ad skipped")
        except:
            print("No ad to skip")

        # Wait for 5 seconds to ensure the ad is skipped
        time.sleep(5)

    
    def run_test(self):
        self.searches()
        self.skip_ad()

# Uncomment the below lines to test the search independently
# if __name__ == "__main__":
#     email = 'yt.at.automation@gmail.com'
#     password = 'YoutubeAuto@123'
#     phone_number = '7338219832'
#     youtube_test = YoutubeSkipTest(email, password, phone_number)
#     youtube_test.run_test()

    
    
