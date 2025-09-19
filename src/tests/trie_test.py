import unittest
import random
from trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.t = Trie(2)
        self.t.insert_helper(["minä", "menen", "kouluun", "nyt."])
        self.t.insert_helper(["minä", "menen", "kotiin", "heti."])

    def test_trie_structure(self):
        
        self.assertEqual(str(self.t.root), "Node(freq=0, children=['minä', 'menen', 'kouluun', 'kotiin'], is_terminal=False)")
        
        self.t.insert_helper(["ostan", "muutaman", "jäätelön"])
        self.assertEqual(str(self.t.root), "Node(freq=0, children=['minä', 'menen', 'kouluun', 'kotiin', 'ostan', 'muutaman'], is_terminal=False)")
        self.assertEqual(str(self.t.root.children["ostan"]), "Node(freq=1, children=['muutaman'], is_terminal=False)")

    def test_trie_find(self):
        x = self.t.find(["menen"])

        self.assertEqual(x, (["kouluun", "kotiin"], [1, 1], [False, False]))

    def test_trie_predict(self):
        random.seed(10)
        prediction = self.t.predict(["minä"], 2)

        self.assertEqual(prediction, (['minä', 'menen', 'kouluun', 'nyt'], [False, False, False, True])) 

    def test_max_attempts(self):
        trie = Trie(3)
        trie.insert_helper(["minä", "menen", "kouluun", "nyt."])
        trie.insert_helper(["minä", "menen", "kotiin", "heti."])

        x = trie.predict(["minä"], 10)
        print(x)
        self.assertEqual(len(x[0]), 13)

    def test_find_and_predict(self):
        random.seed(10)
        self.t.insert_helper(["minä", "ostan", "muutaman", "jäätelön."])
        x = self.t.find(["minä"])

        self.assertEqual(x, (["menen", "ostan"], [2, 1], [False, False]))

        y = self.t.predict(["minä"], 1)

        self.assertEqual(y[0], ['minä', 'menen', 'kouluun', 'nyt'])
        