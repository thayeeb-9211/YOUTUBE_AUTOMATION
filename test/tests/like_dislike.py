import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from play import YoutubeplayTest  # Import the YoutubePlayTest class


class YoutubelikedislikeTest(unittest.TestCase):

    def __init__(self, email, password, phone_number):
        super().__init__()
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.driver = None


    def plays(self):
        # Initialize and run YoutubeplayTest
        self.playing = YoutubeplayTest(self.email, self.password, self.phone_number)
        self.playing.run_test()
        self.driver = self.playing.driver


    def like_dislike(self):
        driver = self.driver

       # Locate and click the like button
        try:
            like_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="top-level-buttons-computed"]/segmented-like-dislike-button-view-model/yt-smartimation/div/div/like-button-view-model/toggle-button-view-model/button-view-model/button'))
            )
            like_button.click()
            print("Video liked")
        except:
            print("Like button not found")
        time.sleep(10)

        # Locate and click the dislike button
        try:
            dislike_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="top-level-buttons-computed"]/segmented-like-dislike-button-view-model/yt-smartimation/div/div/dislike-button-view-model/toggle-button-view-model/button-view-model/button'))
            )
            dislike_button.click()
            print("Video disliked")
        except:
            print("Dislike button not found")
        time.sleep(10)
    
    
    def run_test(self):
        
        self.plays()  
        self.like_dislike()

# Uncomment the below lines to test the like/dislike functionality independently
# if __name__ == "__main__":
#     email = 'yt.at.automation@gmail.com'
#     password = 'YoutubeAuto@123'
#     phone_number = '7338219832'
#     youtube_test = YoutubelikedislikeTest(email, password, phone_number)
#     youtube_test.run_test()