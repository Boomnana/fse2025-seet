import unittest

from driver.driver import *


class StartEnd(unittest.TestCase):
    def setUp(self):
        self.driver=getChromeDriver()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.close()
        self.driver.quit()