import unittest
import timeit
import random

from trie import Trie
from data_parser import DataParser

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.t = Trie(4)
        self.d = DataParser()

    # testataan toimiiko sekä trie-puun opettaminen että siitä ennustaminen tarvittavan nopeasti
    def test_learning_and_prediction_performance(self):
        random.seed(1)

        source = self.d.open_file("kalevala.txt")
        feed = self.d.parser(source)
        insert_time = timeit.timeit(lambda: self.t.insert_helper(feed), number=1)

        self.assertLess(insert_time, 5)

        prediction_time = timeit.timeit(lambda: self.t.predict(["where"], 100000), number=1)

        self.assertLess(prediction_time, 5)

        p = self.t.predict(["where"], 5)
        s = self.d.collect_from_list(p)

        self.assertEqual(s, "Where the red milk had been sprinkled.")