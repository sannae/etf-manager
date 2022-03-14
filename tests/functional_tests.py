import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import unittest

# Shut webdriver manager logs up
os.environ['WDM_LOG_LEVEL'] = '0'

class NewVisitorTest(unittest.TestCase):

    # Start a new headless Chrome browser session
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Close the browser session
    def tearDown(self):
        self.browser.quit()
        
    # Test the website title
    def test_home_page(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('ETF', self.browser.title)

if __name__ == '__main__':  
    unittest.main()