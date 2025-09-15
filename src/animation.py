import time
import sys

class Animate_text:
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
    a = Animate_text()
    a.one_by_one("hello")