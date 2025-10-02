import unittest
import random
from data_parser import DataParser

class TestDataParser(unittest.TestCase):
    def setUp(self):
        self.d = DataParser()
        self.data = """This is. A sample text!"""
        self.word_data = "test"

    # testataan, että data pilkotaan oikein
    def test_parser(self):
        parset_data = self.d.parser(self.data)

        self.assertEqual(parset_data[0:3], ["This", "is.", "A"])
        self.assertEqual(parset_data[-2:], ["sample", "text!"])

    # testataan toimiiko tiedoston avaus oikein
    def test_open_file(self):
        f = self.d.open_file("test.txt")

        self.assertEqual(f[0], "%")

    # testataan toimiiko listasta ja lauseiden päätteistä kerääminen oikein
    def test_collect(self):
        random.seed(10)

        parset_data = self.d.parser(self.data)
        print(parset_data)
        booleans = [False, True, False, False, True]
        collected = self.d.collect_from_list((parset_data, booleans))

        self.assertEqual(collected[0:38], "This is.. A sample text!.")

    # testataan toimiiko kirjaimista kerääminen oikein
    def test_word_to_chars(self):
        x = self.d.word_to_chars(self.word_data)
        y = self.d.collect_letters_from_list(x)

        self.assertEqual(x, ['t', 'e', 's', 't.'])
        self.assertEqual(y, 'test.')

    # testaan poistuuko spesiaalimerkit oikein
    def test_parser_special_chars(self):
        new_data = "this. has_! some0 _weird¤ symbols& right?"

        x = self.d.parser(new_data)

        self.assertEqual(x, ['this.', 'has', 'some', 'weird', 'symbols', 'right?'])