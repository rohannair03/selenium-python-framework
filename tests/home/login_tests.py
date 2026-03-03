from pages.home.login_page import LoginPage
import unittest
import pytest
from utilities.teststatus import TestStatus

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.test_status = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login(email="test@email.com", password="abcabc")
        result1 = self.lp.verifyLoginTitle()
        self.test_status.mark(result1, "Title is incorrect")
        result2 = self.lp.verifyLoginSuccessful()
        self.test_status.markFinal("test_validLogin",result2, "Login unsuccessful")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.logout()
        self.lp.login(email="test@email.com", password="abccba")
        result = self.lp.verifyLoginFailed()
        assert result == True
