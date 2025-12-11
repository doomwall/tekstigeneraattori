import unittest
from trie import Trie
from data_parser import DataParser

class FakeRandom:
    def __init__(self, choices_return=None):
        self.choices_return = choices_return
    
    def return_choices(self, population, weights=None, k=1):
        if self.choices_return is not None:
            return [self.choices_return]
        return [0]

class TestBorder(unittest.TestCase):
    def setUp(self):
        self.t = Trie(3)
        self.d = DataParser()

        self.source = self.d.open_file("kalevala.txt")
        self.cleaned = self.d.clean_text_to_words(self.source)
        self.feed = self.d.parser(self.source)
        self.t.insert_helper(self.feed)

    # testataan find palauttaa yhden vaihtoehdon
    def test_find_always_returns_one_option_and_true(self):
        def test_function(param):
            return (["a"], [100], [True])

        result, terminals = self.t.predict(["word"], 10, find_func=test_function)

        self.assertGreater(len(result), 1)
        self.assertTrue(all(x == "a" for x in result[1:]))
        self.assertEqual(terminals[1:], [True] * (len(result)-1))
        self.assertEqual(len(result), 11)
        self.assertEqual(len(terminals), 11)

    # freqs listassa on nolla-arvoisia arvoja, niin ohjelma valitsee niistä sen mikä on > 0. 
    # Tässä tapauksessa se valitsee aina c.
    def test_find_returns_zeros_in_freqs(self):
        def test_function(param):
            return (["a", "b", "c"], [0, 0, 5], [True, True, False])
        
        fake_rng = FakeRandom(choices_return=2)
        
        result, terminals = self.t.predict(["word"], 5, find_func=test_function, rand_func=fake_rng.return_choices)

        self.assertGreater(len(result), 1)
        self.assertTrue(all(x == "c" for x in result[1:]))
        self.assertTrue(all(t is False for t in terminals[1:]))

    def test_max_attempts(self):
        def test_function(param):
            return (["a"], [100], [False])
        
        result, terminals = self.t.predict(["word"], 10, find_func=test_function)
        self.assertGreater(len(result), 1)
        self.assertLessEqual(len(result), 21)

    def test_find_always_returns_none(self):
        def test_function(param):
           return None
        
        # testataan kutsuuko ohjelma generate_random funktiota
        self.t.generate_random = lambda: (["R"], None, [False])
        
        result, terminals = self.t.predict(["word"], 1, find_func=test_function)
        self.assertGreater(len(result), 0)
        self.assertEqual(result[0], "R")

    def test_find_returns_empties(self):
        def test_function(param):
           return ([], [], [])
        
        # testataan kutsuuko ohjelma generate_random funktiota
        self.t.generate_random = lambda: (["R"], None, [False])
        
        result, terminals = self.t.predict(["word"], 1, find_func=test_function)
        self.assertGreater(len(result), 0)
        self.assertEqual(result[0], "R")