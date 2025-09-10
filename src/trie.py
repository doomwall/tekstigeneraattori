import random

class Node:
    def __init__(self):
        self.children = {}
        self.frequency: int = 0
        self.isTerminal: bool = False

    def __repr__(self):
        return (f"Node(freq={self.frequency}, "
                f"isTerminal={self.isTerminal}, "
                f"children={list(self.children.keys())})")


class Trie:
    def __init__(self, n):
        self.root = Node()
        self.n = n

    def insert(self, data: str):
        current = self.root
        for i in data:
            if i not in current.children:
                current.children[i] = Node()
            current = current.children[i]
            current.frequency += 1

    def insert_helper(self, data):
        for i in range(len(data) - self.n + 1):
            ngram = data[i:i+self.n]
            self.insert(ngram)

    def find(self, input):
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
        result = ""
        result_find = self.find(thing)
        if result_find == None:
            return None
        found_word = random.choices(result_find[0], weights=result_find[1], k=1)[0]
        result += found_word
        result += " "
        amount -= 1
        if amount > 0:
            next_pred = self.predict([found_word], amount)
            if next_pred:
                result += next_pred
        return result


if __name__ == "__main__":
    trie = Trie(n=2)
    trie.insert_helper(["minä", "menen", "kouluun", "nyt", "heti"])
    trie.insert_helper(["minä", "menen", "kotiin", "huomenna", "ehkä"])
    print(trie.root.children)

    prediction = trie.predict(["minä"], 10)
    print(prediction)

    data = ['The', 'inhabitants', 'are', 'strong', 'and', 'hardy', 'with', 'bright', 'intelligent', 'faces', 'high', 'cheek', 'bones', 'yellow']

    trie.insert_helper(data)
    print(trie.root.children)
    prediction = trie.predict(["sleep"], 10)
    print(prediction)