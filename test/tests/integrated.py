#This is the final integrated test which includes all the test cases implemented.

import time
import unittest
from comment import YoutubeCommentTest

class YoutubeintegratedTest(unittest.TestCase):

    def __init__(self, email, password, phone_number):
        super().__init__()
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.driver = None

    def till_commented(self):
        
        #initialize and run YoutubeCommentTest
        self.commented= YoutubeCommentTest(self.email, self.password, self.phone_number)
        self.commented.run_test()
        self.driver = self.commented.driver
        time.sleep(10)
    
    def run_test(self):
        self.till_commented()

# Uncomment the below lines to test the subscribe button functionality independently
if __name__ == "__main__":
    email = 'yt.at.automation@gmail.com'
    password = 'YoutubeAuto@123'
    phone_number = '7338219832'
    youtube_test = YoutubeintegratedTest(email, password, phone_number)
    youtube_test.run_test()
