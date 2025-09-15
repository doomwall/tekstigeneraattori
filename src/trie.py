import random

class Node:
    def __init__(self):
        self.children = {}
        self.frequency: int = 0
        self.is_terminal: bool = False

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
            thing = i.lower()
            if thing not in current.children:
                current.children[thing] = Node()
            current = current.children[thing]
            current.frequency += 1

    def insert_helper(self, data):
        # funktio, joka pilkkoo lisättävän materiaalin puuhun n arvon mukaan
        for i in range(len(data) - self.n + 1):
            ngram = data[i:i+self.n]
            self.insert(ngram)

    def find(self, data):
        # etsii Trie puusta solmun ja palauttaa sen lapset ja niiden yleisyyden
        things = []
        freqs = []
        current = self.root
        for thing in data:
            if thing not in current.children:
                return None
            current = current.children[thing]

        if not current.children:
            # jos solmulla ei ole enempää lapsia, niin palautetaan random sana
            children = list(self.root.children.keys())
            word = random.choice(children)
            return ([word], [1])

        for i, p in current.children.items():
            things.append(i)
            freqs.append(p.frequency)
        return (things, freqs)


    def predict(self, thing, amount):
        # etsii solmuista seuraavia sanoja, joita käyttää lauseessa
        # thing = syötettävä arvo, millä etsitään
        # amount = montako sanaa/merkkiä tuotetaan

        result = thing
        amount = amount - 1

        while amount > 0:
            used_arg = result[-(self.n - 1):] if self.n > 1 else []
            result_find = self.find(used_arg)
            if result_find is None:
                amount -= 1
                continue
            found_word = random.choices(result_find[0], weights=result_find[1], k=1)[0]
            result.append(found_word)
            amount -= 1

        return result




if __name__ == "__main__":
    trie = Trie(n=1)
    trie.insert_helper(["minä", "menen", "kouluun", "nyt", "heti"])
    trie.insert_helper(["minä", "menen", "kotiin", "huomenna", "ehkä"])
    trie.insert_helper(["ehkä", "menen", "sittenkin", "huomenna", "kotiin"])

    prediction = trie.predict(["minä"], 10)
    print(prediction)

    x = trie.predict(["minä"], 10)

    print(x)
