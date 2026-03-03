from pages.home.login_page import LoginPage
import unittest
import pytest
from utilities.teststatus import TestStatus
from pages.courses.register_courses_pages import RegisterCoursesPage
from ddt import ddt, data, unpack
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript", "4538 2635 6429 4014", "0827", "647"), ("Python 3", "1010", "6729", "999"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCvv):
        self.courses.enrollCourse(courses=courseName)
        self.courses.enterCardDetails(cc_num=ccNum, cc_exp=ccExp, cc_cvv=ccCvv)
        #result = self.courses.verifyEnrollFailed()
        #self.ts.markFinal("test_validEnroll", result, "Enroll did not fail")
        self.driver.find_element(By.XPATH, "//a[normalize-space()='ALL COURSES']").click()