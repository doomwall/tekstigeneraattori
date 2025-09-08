class Node:
    def __init__(self, thing = None):
        self.thing = thing
        self.children = {}
        self.frequency: int = 0
        self.isTerminal: bool = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = Node()
            current = current.children[char]
            current.frequency += 1
            

    def find(self, word):
        current = self.root
        for char in word:
            if char == "a":
                print(current.children["a"].frequency)
            if char not in current.children:
                return None
            current = current.children[char]
        return current.children


if __name__ == "__main__":
    puu = Trie()
    puu.insert("apple")
    puu.insert("auto")
    print(puu.find("apple"))