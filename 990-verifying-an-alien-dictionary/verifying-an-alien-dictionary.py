class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {order[i]:i for i in range(len(order))}
        def compare(word):
            return [order_index[c] for c in word]
        return words == sorted(words, key=compare)