from data_parser import Data_parser
from trie import Trie

trie = Trie(n=3)
pars = Data_parser()

source = pars.open_file("kalevala.txt")
feed = pars.parser(source)

trie.insert_helper(feed)

print("Welcome to tekstigeneraattori")

while True:
    word = (input("Give me a word: "))
    if word == "":
        break

    prediction = trie.predict([word], 20)
    print(word, prediction)