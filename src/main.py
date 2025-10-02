from InquirerPy import inquirer # type: ignore
from data_parser import DataParser
from trie import Trie
from animation import AnimateText


ASCII_ART = r""" _____     _        _   _                                       _   _             _
/__   \___| | _____| |_(_) __ _  ___ _ __   ___ _ __ __ _  __ _| |_| |_ ___  _ __(_)
  / /\/ _ \ |/ / __| __| |/ _` |/ _ \ '_ \ / _ \ '__/ _` |/ _` | __| __/ _ \| '__| |
 / / |  __/   <\__ \ |_| | (_| |  __/ | | |  __/ | | (_| | (_| | |_| || (_) | |  | |
 \/   \___|_|\_\___/\__|_|\__, |\___|_| |_|\___|_|  \__,_|\__,_|\__|\__\___/|_|  |_|
                          |___/                                                     """


def main():
    # pääohjelma

    print(ASCII_ART)
    print("\n Welcome to tekstigeneraattori")
    print("""
    This program uses text data sourced from Project Gutenberg (https://www.gutenberg.org),
    a digital library offering public domain literature freely available for use.

    Note: While Project Gutenberg provides public domain content, users are encouraged to review
    its terms of use at: https://www.gutenberg.org/policy/license.html
    """)


    while True:
        decision = inquirer.select(
            message="Choose the material: ",
            choices=["Books", "Kalevala", "Dog names", "Exit"],
        ).execute()

        if decision == "Kalevala":
            kalevala()

        if decision == "Dog names":
            dogs()

        if decision == "Books":
            books()

        if decision == "Exit":
            break

def markov_order():
    # kysyy käyttäjältä Markovin ketjun asteen
    while True:
        order = inquirer.text(message="Give me Markov order: ").execute()
        try:
            trie = Trie(n=int(order))
            return trie
        except ValueError:
            print("Please give a number")

def kalevala():
    # aloittaa ohjelman englannin kielisellä Kalevalalla

    pars = DataParser()
    anim = AnimateText()

    trie = markov_order()

    source = pars.open_file("kalevala.txt")
    feed = pars.parser(source)
    trie.insert_helper(feed)

    how_many_message = "How many words shold I generate atleast?"

    while True:
        print("Choose the word you want to start with.")
        print("If the word is not found from material, a random word is used instead")
        word = inquirer.text(message="Give me a starting word (empty will close):").execute()
        if word == "":
            break

        amount = how_many(how_many_message)

        prediction = trie.predict([word], int(amount))
        collected = pars.collect_from_list(prediction)

        if len(prediction) == 1:
            print("This word was not found in the text")
        else:
            anim.one_by_one(collected)

def books():
    # aloittaa ohjelman neljällä eri kirjalla

    pars = DataParser()
    anim = AnimateText()

    trie = markov_order()

    for i in ["alice.txt", "frankenstein.txt", "moby_dick.txt", "pride.txt"]:
        source = pars.open_file(i)
        feed = pars.parser(source)
        trie.insert_helper(feed)

    how_many_message = "How many words shold I generate atleast?"

    while True:
        print("Choose the word you want to start with.")
        print("If the word is not found from material, a random word is used instead")
        word = inquirer.text(message="Give me a starting word (empty will close):").execute()
        if word == "":
            break

        amount = how_many(how_many_message)

        prediction = trie.predict([word], int(amount))
        collected = pars.collect_from_list(prediction)

        if len(prediction) == 1:
            print("This word was not found in the text")
        else:
            anim.one_by_one(collected)

def dogs():
    # aloittaa ohjelman koirien nimillä

    pars = DataParser()

    trie = markov_order()
    how_many_message = "How many letters atleast should the name have:"

    source = pars.open_file("dogs.txt")
    feed = pars.parser(source)
    for i in feed:
        char = pars.word_to_chars(i)
        trie.insert_helper(char)

    while True:
        print("Choose the letter you want to start with.")
        letter = inquirer.text(message="Give me a starting word (empty will close):").execute()
        if letter == "":
            break

        amount = how_many(how_many_message)

        prediction = trie.predict([letter], int(amount))
        collected = pars.collect_letters_from_list(prediction[0])

        if len(prediction) == 1:
            print("This letter was not found in the text")
        else:
            print(collected)
            print("")


def how_many(message):
    while True:
        try:
            amount = inquirer.number(message=message).execute()
            return int(amount)
        except ValueError:
            print("Only numbers are allowed.")


if __name__ == "__main__":
    main()
