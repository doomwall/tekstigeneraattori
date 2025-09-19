from pathlib import Path
import re, random

# Tämä luokka pilkkoo datan hyväksyttävään muotoon Trie puuta varten

class DataParser:
    def __init__(self):
        self.dirname = Path(__file__).resolve().parent.parent

    def parser(self, data):
        # regex, joka erottelee tekstin sanoiksi ja palauttaa listan
        return re.findall(r'[^\W\d_]+[;.,!?]?', data, re.UNICODE)

    def word_to_chars(self, data):
        # pilkkoo sanan kirjaimiksi ja lisää viimeiseen kirjaimeen pisteen = isTerminal = True
        new_data = list(data)
        new_data[-1] = new_data[-1] + "."
        return new_data

    def open_file(self, filename):
        # avaa tiedoston ja lukee sisällön
        path = str(self.dirname) + "/material/" + filename
        with open(path, encoding="utf-8") as f:
            return f.read()

    def collect_from_list(self, data):
        # muuntaa listan sanoja ja booleans tulostettavaan muotoon
        # funktiolle syötettävä data on oltava muodossa ([words], [booleans])
        # tällä tavalla oikea arvo is_terminal löytää oikean sanan

        result = ""
        thing_list = data[0]
        booleans = data[1]
        capital = True
        for i in range(0, len(thing_list)-1):
            if capital:
                result += thing_list[i].capitalize()
                capital = False
            else:
                result += thing_list[i]

            if booleans[i] is True and random.random() < 0.6:
                result += "."
                capital = True
            result += " "

        result += thing_list[-1] + "."
        return result

    def collect_letters_from_list(self, data):
        return "".join(data)