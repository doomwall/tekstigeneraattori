import random

class Node:
    def __init__(self):
        self.children = {}
        self.frequency: int = 0
        self.isTerminal: bool = False

    def __repr__(self):
        return (f"Node(freq={self.frequency}, "
                f"children={list(self.children.keys())})")


class Trie:
    def __init__(self, n):
        self.root = Node()
        self.n = n  # Markovin asteen määrä 

    def insert(self, data: str):
        # funktio arvojen lisäämiselle Trie-puuhun
        current = self.root
        for i in data:
            if i not in current.children:
                current.children[i] = Node()
            current = current.children[i]
            current.frequency += 1

    def insert_helper(self, data):
        # funktio, joka pilkkoo lisättävän materiaalin puuhun n arvon mukaan
        for i in range(len(data) - self.n + 1):
            ngram = data[i:i+self.n]
            self.insert(ngram)

    def find(self, input):
        # etsii Trie puusta solmun ja palauttaa sen lapset ja niiden yleisyyden
        things = []
        freqs = []
        current = self.root
        for thing in input:
            if thing not in current.children:
                return None
            current = current.children[thing]

        if not current.children:
            return None
        for i, p in current.children.items():
            things.append(i)
            freqs.append(p.frequency)
        return (things, freqs)
    

    def predict(self, thing, amount):
        result = thing

        while amount > 0:
            used_arg = result[-(self.n - 1):]
            result_find = self.find(used_arg)
            if result_find == None:
                amount -= 1
                continue
            found_word = random.choices(result_find[0], weights=result_find[1], k=1)[0]
            result.append(found_word)
            amount -= 1

        return result
            



if __name__ == "__main__":
    trie = Trie(n=3)
    trie.insert_helper(["minä", "menen", "kouluun", "nyt", "heti"])
    trie.insert_helper(["minä", "menen", "kotiin", "huomenna", "ehkä"])
    trie.insert_helper(["ehkä", "menen", "sittenkin", "huomenna", "kotiin"])

    #prediction = trie.predict(["minä"], 10)
    #print(prediction)

    x = trie.predict(["minä"], 10)

    print(x)