import unittest
import subprocess


class TestRiskReportTestCases(unittest.TestCase):
    def test_riskreport_testcase_rs519113(self):
        status = subprocess.call('test/test_riskreport_testcase_rs519113.sh')
        self.assertEqual(status, 0)


def test_all():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TestRiskReportTestCases))
    return suite
