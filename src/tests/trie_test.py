import unittest
from trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.t = Trie(2)
        self.t.insert_helper(["minä", "menen", "kouluun", "nyt"])
        self.t.insert_helper(["minä", "menen", "kotiin", "heti"])

    def test_trie_structure(self):
        
        self.assertEqual(str(self.t.root), "Node(freq=0, children=['minä', 'menen', 'kouluun', 'kotiin'])")
        
        self.t.insert_helper(["ostan", "muutaman", "jäätelön"])
        self.assertEqual(str(self.t.root), "Node(freq=0, children=['minä', 'menen', 'kouluun', 'kotiin', 'ostan', 'muutaman'])")
        self.assertEqual(str(self.t.root.children["ostan"]), "Node(freq=1, children=['muutaman'])")

    def test_trie_find(self):
        x = self.t.find(["menen"])
        y = self.t.find(["heti"])

        self.assertEqual(x, (["kouluun", "kotiin"], [1, 1]))
        self.assertEqual(y, None)

    def test_trie_predict(self):
        prediction = self.t.predict(["minä"], 1)

        self.assertEqual(prediction, ["minä", "menen"]) 