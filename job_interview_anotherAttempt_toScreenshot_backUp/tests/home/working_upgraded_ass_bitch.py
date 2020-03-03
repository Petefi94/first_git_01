from pages.home.login_page_template import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)


    # Need to verify two verification points
    # 1 fails, code will not go to the next verification point
    # If assert fails, it stops current test execution and
    # moves to the next test method
    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("dusanpet.94@gmail.com", "letskodeit94")
        result1 = self.lp.verifyTitle()
        self.ts.mark(result1, "Title Verfication")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login Verification")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("dusanpet.94@gmail.com", "letskodeit94")
        result = self.lp.verifyLoginFailed()
        assert result == True