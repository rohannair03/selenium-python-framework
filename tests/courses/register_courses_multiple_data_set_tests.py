from pages.home.navigation_page import NavigationPage
import unittest
import pytest
from utilities.teststatus import TestStatus
from pages.courses.register_courses_pages import RegisterCoursesPage
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript", "4538 2635 6429 4014", "0827", "647"), ("Python 3", "1010", "6729", "999"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCvv):
        self.courses.enrollCourse(courses=courseName)
        self.courses.enterCardDetails(cc_num=ccNum, cc_exp=ccExp, cc_cvv=ccCvv)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enroll did not fail")
        self.nav.navigateToAllCourses()