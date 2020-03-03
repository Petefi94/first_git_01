from pages.home.login_page_template import LoginPage
from pages.home.login_page_01 import LoginPage01
from pages.home.login_page_02 import LoginPage02
from base.selenium_driver import SeleniumDriver
from utilities.teststatus import TestStatus
import unittest
import pytest
import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    # auto-use is here so every test inherits it
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        # other page
        self.lp_01 = LoginPage01(self.driver)
        self.lp_02 = LoginPage02(self.driver)
        # self.sd = SeleniumDriver(self.driver) -> Not necessary

    # Need to verify two verification points
    # 1 fails, code will not go to the next verification point
    # If assert fails, it stops current test execution and
    # moves to the next test method

    @pytest.mark.run(order=1)
    def test_validLogin_01(self):
        self.lp_01.clickLoginLink()
        time.sleep(2)
        self.lp_01.enterEmail("dusanpet.94@gmail.com")
        time.sleep(2)
        self.lp_01.justClick()
        time.sleep(2)
        self.lp_01.enterPassword("123123")
        time.sleep(2)
        self.lp_01.clickLoginButton()
        time.sleep(2)
        # This is where the pop-up happens
        time.sleep(1)
        self.lp_01.elementPresent()
        time.sleep(1)
        self.lp_01.justClick_2()
        time.sleep(3)

        result1 = self.lp_01.verifyContains()
        self.ts.mark(result1, "Login Verification")
        self.ts.markFinal("test_validLogin", result1, "Login Verification")

    @pytest.mark.run(order=2)
    def test_validLogin_02(self):
        result1 = self.lp_02.verifyContains()
        self.ts.mark(result1, "Header Verification")
        self.ts.markFinal("test_validLogin", result1, "Login Verification")









