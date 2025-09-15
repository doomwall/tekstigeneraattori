from pathlib import Path
import re

# Tämä luokka pilkkoo datan hyväksyttävään muotoon Trie puuta varten

class DataParser:
    def __init__(self):
        self.dirname = Path(__file__).resolve().parent.parent

    def parser(self, data):
        return re.split(r'\W+', data)

    def word_to_chars(self, data):
        return list(data)

    def open_file(self, filename):
        path = str(self.dirname) + "/material/" + filename
        with open(path, encoding="utf-8") as f:
            return f.read()

    def collect_from_list(self, data):
        result = ""
        for i in data:
            result += i
            result += " "

        return result

    def collect_letters_from_list(self, data):
        return "".join(data)



if __name__ == "__main__":
    d = DataParser()
    x = d.open_file("kalevala.txt")

    d = DataParser()
    x = d.word_to_chars("hello")
    print(x)
