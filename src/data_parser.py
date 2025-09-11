from pathlib import Path
import re

# Tämä luokka pilkkoo datan hyväksyttävään muotoon Trie puuta varten

class Data_parser:
    def __init__(self):
        self.dirname = Path(__file__).resolve().parent.parent

    def parser(self, data):
        return re.split(r'\W+', data)

    def open_file(self, filename):
        print(str(self.dirname) + "/material/" + filename)
        f = open(str(self.dirname) + "/material/" + filename, encoding="utf-8")
        return f.read()
    
    def collect_from_list(self, data):
        result = ""
        for i in data:
            result += i
            result += " "

        return result



if __name__ == "__main__":
    d = Data_parser()
    x = d.open_file("kalevala.txt")

    print(x)

    y = d.parser(x)

    print(y)

    p = d.collect_from_list(y)

    print(p)

