from data_parser import Data_parser
from trie import Trie


def main():
    pars = Data_parser()

    source = pars.open_file("kalevala.txt")
    feed = pars.parser(source)

    print("Welcome to tekstigeneraattori")
    while True:
        order = input("Give me Markov order: ")
        try:
            trie = Trie(n=int(order))
            trie.insert_helper(feed)
            break
        except:
            print("Please give a number")
    
    while True:
        word = input("Give me a word: ")
        if word == "":
            break

        amount = input("Give me how many words you want: ")

        prediction = trie.predict([word], int(amount))
        collected = pars.collect_from_list(prediction)

        if len(prediction) == 1:
            print(f"This word was not found in the text")
        else:
            print(collected)

if __name__ == "__main__":
    main()