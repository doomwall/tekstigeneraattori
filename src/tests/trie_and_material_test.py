import unittest
from trie import Trie
from data_parser import DataParser


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.t = Trie(3)
        self.d = DataParser()

        self.source = self.d.open_file("kalevala.txt")
        feed = self.d.parser(self.source)
        self.t.insert_helper(feed)

    def test_ngram_found_from_source_material(self):
        result = "seek "
        a = self.t.collect_children(self.t.root.children["seek"])
        for i in a[0]:
            result += f"{i} "

        result = result[:-1]

        self.assertEqual(result, "seek my forest")

        result2 = "seek "
        for i in a[3]:
            result2 += f"{i} "

        result2 = result2[:-1]

        self.assertEqual(result2, "seek a butcher")

        self.assertTrue(result in self.source)
        self.assertTrue(result2 in self.source)
        self.assertFalse("seek my butcher" in self.source)