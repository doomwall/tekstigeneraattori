import unittest
from trie import Trie
from data_parser import DataParser


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.t = Trie(3)
        self.d = DataParser()

        self.source = self.d.open_file("kalevala.txt")
        self.cleaned = self.d.clean_text_to_words(self.source)
        self.feed = self.d.parser(self.source)
        self.t.insert_helper(self.feed)

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

    # tarkistaa löytyykö n-gram ikkunat materiaalista
    # HUOM! On mahdollista, että tämä testi epäonnistuu jollain toisella sanalla kuin "I"
    # koska ohjelma käyttää random sanaa generoimiseen, jos jatkoa ei löydy.
    # Sana "I" on niin yleinen, että sille on paljon jatkoa aina.
    def test_all_ngrams_from_generation_found_from_source(self):
        # alustetaan triet asteilla 1 ja 4
        t1 = Trie(2)
        t4 = Trie(5)

        t1.insert_helper(self.feed)
        t4.insert_helper(self.feed)

        predict_t1 = t1.predict(["I"], 10)[0]

        for i in range(0, len(predict_t1)):
            boundary = i+2
            if boundary > len(predict_t1):
                break
            
            window = predict_t1[i:boundary]
            words = " ".join(window)

            self.assertTrue(words in self.cleaned)

        predict_t4 = t4.predict(["I"], 10)[0]

        for i in range(0, len(predict_t4)):
            boundary = i+5
            if boundary > len(predict_t4):
                break
            
            window = predict_t4[i:boundary]
            words = " ".join(window)

            self.assertTrue(words in self.cleaned)