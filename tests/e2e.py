import unittest

from selenium import webdriver
from sys import platform
import os


class ScoreTest(unittest.TestCase):
    def setUp(self):
        if platform == "linux" or platform == "linux2":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--window-size=1420,1080')
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            dir_path = os.path.dirname(os.path.realpath(__file__))
            self.driver = webdriver.Chrome(executable_path=dir_path + "/chromedriver", chrome_options=chrome_options)
        elif platform == "win32":
            # chrome_options.add_argument('--headless')
            self.driver = webdriver.Chrome(executable_path="c:/chromedriver.exe")

    def test_scores_service(self):
        self.driver.get("http://127.0.0.1:5000/")
        score_from_web = self.driver.find_element(by="id", value="score").text
        return self.assertTrue(1 <= int(score_from_web) <= 1000)

    def tearDown(self):
        print("Done with session %s" % self.driver.session_id)
        self.driver.quit()


def main_function():
    unittest.main()
