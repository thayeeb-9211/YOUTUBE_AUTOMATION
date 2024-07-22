#comment on the video and end.

import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from share import YoutubeshareTest  # Import the YoutubeShareTest class


class YoutubeCommentTest(unittest.TestCase):

    def __init__(self, email, password, phone_number):
        super().__init__()
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.driver = None


    def sharing(self):
        # Initialize and run YoutubeShareTest
        self.shared = YoutubeshareTest(self.email, self.password, self.phone_number)
        self.shared.run_test()
        self.driver = self.shared.driver

        
    def comment(self):
        driver = self.driver

          # Scroll down by 1000 pixels
        driver.execute_script("window.scrollBy(0, 600);")

         # Try to comment on the video
        try:
            comment_section = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'style-scope ytd-comment-simplebox-renderer'))
            )
            comment_section.click()

            comment_box = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'style-scope ytd-commentbox'))
            )
            
            comment_box.send_keys("Awesome! Good video!")

            comment_button = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Comment" and contains(@class, "yt-spec-button-shape-next yt-spec-button-shape-next--filled yt-spec-button-shape-next--call-to-action yt-spec-button-shape-next--size-m")]'))
            )
            comment_button.click()
            print("Comment posted successfully")
            print("All 8 test cases executed successfully")
            time.sleep(5)
           
        except Exception as e:
            print(f"An error occurred while commenting: {e}")

        time.sleep(15)
    
    
    def run_test(self):
        self.sharing()
        self.comment()

# Uncomment the below lines to test the comment button functionality independently
# if __name__ == "__main__":
    # email = 'Enter_your_Email_here'
    # password = 'Enter_your_Password_here'
    # phone_number = 'Enter_your_Phone_Number_here'
#     youtube_test = YoutubeCommentTest(email, password, phone_number)
#     youtube_test.run_test()