import unittest
from trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.t = Trie(2)
        self.t.insert_helper(["minä", "menen", "kouluun", "nyt"])
        self.t.insert_helper(["minä", "menen", "kotiin", "heti"])

    def test_trie_structure(self):
        test_t = Trie(2)
        test_t.insert_helper(["ostan", "muutaman", "jäätelön"])

        self.assertEqual(str(test_t.root), "Node(freq=0, children=['ostan', 'muutaman'])")
        self.assertEqual(str(test_t.root.children["ostan"]), "Node(freq=1, children=['muutaman'])")

    def test_trie_find(self):
        x = self.t.find(["menen"])

        self.assertEqual(x, (["kouluun", "kotiin"], [1, 1]))

    