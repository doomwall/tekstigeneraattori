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

    # kerää puusta kaikki tietyn noden lehdet ja kokoaa ne printattavaan muotoon
    def collect_tree(self, starting_node, starting_depth = -1, number_of_children = 0):
        how_many = number_of_children
        depth = starting_depth + 1
        print_out = ""

        for child in starting_node.children:
            if depth > 1:
                print_out += (f"\t" * (depth-1))
            if depth > 0:
                print_out += ("  \u255a\u2550\u2550\u2550\u2550\u2550 ")
            print_out += f"{child} \n"

            how_many += 1

            if starting_node.children[child].children:
                a = self.collect_tree(starting_node.children[child], depth)
                print_out += a[0]
                how_many += a[1]

        return (print_out, how_many)
    
    # kerää kaikki tietyn noden lehdet listaksi
    def collect_children(self, starting_node):
        result = []

        for child_name, child_node in starting_node.children.items():
            if child_node.children:
                for subpath in self.collect_children(child_node):
                    result.append([child_name] + subpath)
            else:
                result.append([child_name])

        return result

    # tulostaa koko puun rakenteen
    def __str__(self):
        whole_tree = self.collect_tree(self.root)
        return (f"{whole_tree[0]}"
               f"How many nodes: {whole_tree[1]}")


    # funktio arvojen lisäämiselle Trie-puuhun
    def insert(self, data: str):
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
        # etsii Trie puusta solmun ja palauttaa sen lehdet, frekvenssin ja onko se lauseen/sanan päätös
        things = []
        freqs = []
        is_terminals = []
        current = self.root
        for i in data:
            if i not in current.children:
                return None
            current = current.children[i]

        if not current.children:
            # jos solmulla ei ole lapsia, palautetaan tyhjä
            return None

        for i, p in current.children.items():
            things.append(i)
            freqs.append(p.frequency)
            is_terminals.append(p.is_terminal)
        return (things, freqs, is_terminals)
    
    # palauttaa random vaihtoehdon puun arvoista
    def generate_random(self):
        fallback = random.choice(list(self.root.children.items()))
        return ([fallback[0]], [fallback[1].frequency], [fallback[1].is_terminal])

    def predict(self, thing, amount, find_func=None, rand_func=None):
        # etsii solmuista seuraavia arvoja, joita käyttää lopputuloksessa
        # thing = syötettävä arvo, millä etsitään
        # amount = montako sanaa/merkkiä tuotetaan

        result = thing
        booleans = [False]
        amount = amount - 1

        # näillä tarkistetaan kutsutaanko funktiota injektioilla
        if find_func is None:
            find_func = self.find

        if rand_func is None:
            rand_func = random.choices

        # annetaan ohjelmalle maksimi määrä sanoille, jos se ei löydä sanaa joka lopettaisi lauseen. 
        max_attempts = amount + 10

        while True and max_attempts > 0:
            used_arg = result[-(self.n - 1):] if self.n > 1 else []
            result_find = find_func(used_arg)

            # jos kysyttyä arvoa ei löydy trie:stä, aloitetaan generointi random arvolla
            if result_find == None or result_find[0] == []:
                random_choice = self.generate_random()
                result = random_choice[0]
                booleans = random_choice[2]
                max_attempts -= 1
                continue

            # arvotaan sana joukosta sanoja käyttäen painotusta frekvenssille
            value = rand_func(
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
    
