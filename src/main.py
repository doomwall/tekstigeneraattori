from data_parser import Data_parser
from trie import Trie
from animation import Animate_text
from InquirerPy import inquirer # type: ignore

ascii_art = """ _____     _        _   _                                       _   _             _
/__   \___| | _____| |_(_) __ _  ___ _ __   ___ _ __ __ _  __ _| |_| |_ ___  _ __(_)
  / /\/ _ \ |/ / __| __| |/ _` |/ _ \ '_ \ / _ \ '__/ _` |/ _` | __| __/ _ \| '__| |
 / / |  __/   <\__ \ |_| | (_| |  __/ | | |  __/ | | (_| | (_| | |_| || (_) | |  | |
 \/   \___|_|\_\___/\__|_|\__, |\___|_| |_|\___|_|  \__,_|\__,_|\__|\__\___/|_|  |_|
                          |___/                                                     """


def main():
    # pääohjelma
    pars = Data_parser()
    

    print(ascii_art)
    print("Welcome to tekstigeneraattori")

    while True:
        decision = inquirer.select(
            message="Choose the material: ",
            choices=["Kalevala", "Dog names", "Exit"],
        ).execute()

        if decision == "Kalevala":
            kalevala()

        if decision == "Dog names":
            dogs()

        if decision == "Exit":
            break

def markov_order():
    # kysyy käyttäjältä Markovin ketjun asteen
    while True:
        order = inquirer.text(message="Give me Markov order: ").execute()
        try:
            trie = Trie(n=int(order))
            return trie
        except:
            print("Please give a number")

def kalevala():
    # aloittaa ohjelman englannin kielisellä Kalevalalla

    pars = Data_parser()
    anim = Animate_text()

    trie = markov_order()

    source = pars.open_file("kalevala.txt")
    feed = pars.parser(source)
    trie.insert_helper(feed)
    while True:
        word = inquirer.text(message="Give me a word: ").execute()
        if word == "":
            break

        amount = inquirer.text(message="How many words would you like to generate: ").execute()

        prediction = trie.predict([word], int(amount))
        collected = pars.collect_from_list(prediction)

        if len(prediction) == 1:
            print(f"This word was not found in the text")
        else:
            anim.one_by_one(collected)

def dogs():
    # aloittaa ohjelman koirien nimillä

    pars = Data_parser()

    trie = markov_order()

    source = pars.open_file("dogs.txt")
    feed = pars.parser(source)
    for i in feed:
        char = pars.word_to_chars(i)
        trie.insert_helper(char)

    while True:
        letter = inquirer.text(message="Give me a letter: ").execute()
        if letter == "":
            break

        amount = inquirer.text(message="How long name would you like to generate: ").execute()

        prediction = trie.predict([letter], int(amount))
        collected = pars.collect_letters_from_list(prediction)

        if len(prediction) == 1:
            print(f"This letter was not found in the text")
        else:
            print(collected)


if __name__ == "__main__":
    main()
