import unittest
import random
from trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.t = Trie(2)
        self.t.insert_helper(["minä", "menen", "kouluun", "nyt."])
        self.t.insert_helper(["minä", "menen", "kotiin", "heti."])

    # testataan että trie-puu on oikeassa rakenteessa
    def test_trie_structure(self):
        
        self.assertEqual(str(self.t.root), "Node(freq=0, children=['minä', 'menen', 'kouluun', 'kotiin'], is_terminal=False)")
        
        self.t.insert_helper(["ostan", "muutaman", "jäätelön"])
        self.assertEqual(str(self.t.root), "Node(freq=0, children=['minä', 'menen', 'kouluun', 'kotiin', 'ostan', 'muutaman'], is_terminal=False)")
        self.assertEqual(str(self.t.root.children["ostan"]), "Node(freq=1, children=['muutaman'], is_terminal=False)")

    # testataan että trie:stä etsiminen toimii
    def test_trie_find(self):
        x = self.t.find(["menen"])

        self.assertEqual(x, (["kouluun", "kotiin"], [1, 1], [False, False]))

    # testataan että ennakoiminen toimii oikein
    def test_trie_predict(self):
        random.seed(10)
        prediction = self.t.predict(["minä"], 2)

        self.assertEqual(prediction, (['minä', 'menen', 'kouluun', 'nyt'], [False, False, False, True])) 

    # testaan ettei generoida liikaa sanoja
    def test_max_attempts(self):
        trie = Trie(3)
        trie.insert_helper(["minä", "menen", "kouluun", "nyt."])
        trie.insert_helper(["minä", "menen", "kotiin", "heti."])

        x = trie.predict(["minä"], 10)
        print(x)
        self.assertEqual(len(x[0]), 3)

    # testataan lisäämistä ja generointia yhdessä
    def test_find_and_predict(self):
        random.seed(10)
        self.t.insert_helper(["minä", "ostan", "muutaman", "jäätelön."])
        x = self.t.find(["minä"])

        self.assertEqual(x, (["menen", "ostan"], [2, 1], [False, False]))

        y = self.t.predict(["minä"], 1)

        self.assertEqual(y[0], ['minä', 'menen', 'kouluun', 'nyt'])
        