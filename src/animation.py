import time
import sys

class AnimateText:
    def __init__(self):
        pass

    def one_by_one(self, text):
        # tekee tekstille animaation, jolla se tulostetaan kirjain kerrallaan
        for letter in text:
            print(letter, end='')
            sys.stdout.flush()
            time.sleep(0.05)
        print("\n")


if __name__ == "__main__":
    a = AnimateText()
    a.one_by_one("hello")
