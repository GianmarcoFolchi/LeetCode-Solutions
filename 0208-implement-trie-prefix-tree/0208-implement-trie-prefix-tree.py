class Trie:

    def __init__(self):
        self.nodes = [None] * 26
        self.isWordFlag = False

    def insert(self, word: str) -> None:
        currTrie = self
        for i, c in enumerate(word): 
            cIndex = indexForLetter(c)
            print(type(currTrie))
            if not currTrie.nodes[cIndex]:
                currTrie.nodes[cIndex] = Trie()
            currTrie = currTrie.nodes[cIndex]

            if i == len(word) - 1: 
                currTrie.isWordFlag = True
            
    def search(self, word: str) -> bool:
        currTrie = self
        for i, c in enumerate(word): 
            cIndex = indexForLetter(c)
            if not currTrie.nodes[cIndex]:
                return False
            currTrie = currTrie.nodes[cIndex]

            if i == len(word) - 1 and currTrie.isWordFlag: 
                return True
        
        return False

    def startsWith(self, prefix: str) -> bool:
        currTrie = self
        for i, c in enumerate(prefix): 
            cIndex = indexForLetter(c)
            if not currTrie.nodes[cIndex]:
                return False
            currTrie = currTrie.nodes[cIndex]

            if i == len(prefix) - 1: 
                return True
        
        return False
    

def indexForLetter(char): 
    return ord(char) - ord('a')
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)