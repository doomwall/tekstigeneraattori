import random

class Node:
    def __init__(self):
        # Solmulle annetaan kolme arvoa, solmun lapset, frekvenssi ja onko se syötön pääte
        self.children = {}
        self.frequency: int = 0
        self.is_terminal: bool = False

    def __repr__(self):
        return (f"Node(freq={self.frequency}, "
                f"children={list(self.children.keys())}, "
                f"is_terminal={self.is_terminal})")


class Trie:
    def __init__(self, n):
        self.root = Node()
        self.n = n  # Markovin asteen määrä
        self.endings = [".", ",", "!", ";", "?"]

    def insert(self, data: str):
        # funktio arvojen lisäämiselle Trie-puuhun
        current = self.root
        for i in data:
            thing = i.lower()
            terminal = i[-1] in self.endings # tarkistaa päättyykö annettu arvo erikoismerkkiin

            if terminal:
                thing = thing[:-1] # poistaa erikoismerkin annetusta arvosta

            # jos arvoa ei löydy käsiteltävän solmun lehdistä, sille lisätään sen niminen solmu lapseksi
            if thing not in current.children:
                current.children[thing] = Node()
                current.children[thing].is_terminal |= terminal

            # vaihdetaan käsiteltäväksi solmuksi tämän hetkinen arvo
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
        is_terminals = []
        current = self.root
        for i in data:
            if i not in current.children:
                fallback = random.choice(list(self.root.children.items()))
                return ([fallback[0]], [fallback[1].frequency], [fallback[1].is_terminal])
            current = current.children[i]

        if not current.children:
            # jos solmulla ei ole enempää lapsia, niin palautetaan random sana
            fallback = random.choice(list(self.root.children.items()))
            return ([fallback[0]], [fallback[1].frequency], [fallback[1].is_terminal])

        for i, p in current.children.items():
            things.append(i)
            freqs.append(p.frequency)
            is_terminals.append(p.is_terminal)
        return (things, freqs, is_terminals)


    def predict(self, thing, amount):
        # etsii solmuista seuraavia sanoja, joita käyttää lauseessa
        # thing = syötettävä arvo, millä etsitään
        # amount = montako sanaa/merkkiä tuotetaan

        result = thing
        booleans = [False]
        amount = amount - 1

        # annetaan ohjelmalle maksimi määrä sanoille, jos se ei löydä sanaa joka lopettaisi lauseen. 
        max_attempts = amount + 10

        while True:
            used_arg = result[-(self.n - 1):] if self.n > 1 else []
            result_find = self.find(used_arg)

            # arvotaan sana joukosta sanoja
            value = random.choices(
                list(range(0, len(result_find[0]))),
                weights=result_find[1],
                k=1)[0]

            result.append(result_find[0][value])
            booleans.append(result_find[2][value])
            amount -= 1
            max_attempts -= 1

            # jos määrä ylitetään, lopetetaan etsintä seuraavaan sanaan joka on lauseen päätös
            if amount < 0 and result_find[2][value]:
                break

            if max_attempts == 0:
                break

        return (result, booleans)
