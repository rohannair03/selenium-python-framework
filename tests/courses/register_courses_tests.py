from pages.home.login_page import LoginPage
import unittest
import pytest
from utilities.teststatus import TestStatus
from pages.courses.register_courses_pages import RegisterCoursesPage

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.courses.enrollCourse(courses="JavaScript")
        self.courses.enterCardDetails(cc_num="4538 2643 6429 4014", cc_exp="0827", cc_cvv="647")
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_validEnroll", result, "Enroll did not fail")
        print("Test completed")
