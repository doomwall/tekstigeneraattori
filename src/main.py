from data_parser import Data_parser
from trie import Trie
from animation import Animate_text
from InquirerPy import inquirer

ascii_art = """ _____     _        _   _                                       _   _             _ 
/__   \___| | _____| |_(_) __ _  ___ _ __   ___ _ __ __ _  __ _| |_| |_ ___  _ __(_)
  / /\/ _ \ |/ / __| __| |/ _` |/ _ \ '_ \ / _ \ '__/ _` |/ _` | __| __/ _ \| '__| |
 / / |  __/   <\__ \ |_| | (_| |  __/ | | |  __/ | | (_| | (_| | |_| || (_) | |  | |
 \/   \___|_|\_\___/\__|_|\__, |\___|_| |_|\___|_|  \__,_|\__,_|\__|\__\___/|_|  |_|
                          |___/                                                     """

def main():
    pars = Data_parser()
    anim = Animate_text()
    
    print(ascii_art)
    print("Welcome to tekstigeneraattori")
    while True:
        order = inquirer.text(message="Give me Markov order: ").execute()
        try:
            trie = Trie(n=int(order))
            break
        except:
            print("Please give a number")

    while True:
        decision = inquirer.select(
            message="Choose the material: ",
            choices=["Kalevala", "Dog names"],
        ).execute()
        break
    
    if decision == "Kalevala":
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

if __name__ == "__main__":
    main()