from pathlib import Path
import re, random

# Tämä luokka pilkkoo datan hyväksyttävään muotoon Trie puuta varten

class DataParser:
    def __init__(self):
        self.dirname = Path(__file__).resolve().parent.parent

    def parser(self, data):
        return re.findall(r'\w+[;.,!]?', data)

    def word_to_chars(self, data):
        new_data = list(data)
        new_data[-1] = new_data[-1] + "."
        return new_data

    def open_file(self, filename):
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

            if booleans[i] is True and random.random() < 0.5:
                result += "."
                capital = True
            result += " "

        result += thing_list[-1] + "."
        return result

    def collect_letters_from_list(self, data):
        return "".join(data)



if __name__ == "__main__":
    d = DataParser()
    x = d.open_file("dogs.txt")
    y = d.parser(x)
    print(y)
