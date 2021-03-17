import unittest
from skcolumbia.report import ReportModel


class MyTestCase(unittest.TestCase):
    def test_construction(self):
        name = "Important Report"
        dut = ReportModel(name)
        self.assertIsInstance(dut, ReportModel)
        self.assertEqual(dut.name, name)

    def test_construction_empty(self):
        dut = ReportModel()
        self.assertIsInstance(dut, ReportModel)
        self.assertEqual(dut.name, "")


if __name__ == '__main__':
    unittest.main()
