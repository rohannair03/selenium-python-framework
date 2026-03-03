from pages.home.navigation_page import NavigationPage
import unittest
import pytest
from utilities.teststatus import TestStatus
from pages.courses.register_courses_pages import RegisterCoursesPage
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigateToAllCourses()

    @pytest.mark.run(order=1)
    @data(*getCSVData("C:/Users/rohan/workspace_python/letskodeit/testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCvv):
        self.courses.enrollCourse(courses=courseName)
        self.courses.enterCardDetails(cc_num=ccNum, cc_exp=ccExp, cc_cvv=ccCvv)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_validEnroll", result, "Enroll did not fail")
