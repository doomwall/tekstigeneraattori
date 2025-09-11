import unittest
from data_parser import Data_parser

class TestDataParser(unittest.TestCase):
    def setUp(self):
        self.d = Data_parser()
        self.data = """This is a sample text for the parser. 
        It needs to cut it in blocks without special characters!"""

    def test_parser(self):
        parset_data = self.d.parser(self.data)

        self.assertEqual(parset_data[0:3], ["This", "is", "a"])
        self.assertEqual(parset_data[-2:], ["characters", ""])

    def test_open_file(self):
        f = self.d.open_file("test.txt")

        self.assertEqual(f[0], "%")

    def test_collect(self):
        parset_data = self.d.parser(self.data)

        collected = self.d.collect_from_list(parset_data)

        self.assertEqual(collected[0:36], "This is a sample text for the parser")