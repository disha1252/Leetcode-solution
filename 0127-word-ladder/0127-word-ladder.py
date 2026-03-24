from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList):
        wordSet = set(wordList)
        
        if endWord not in wordSet:
            return 0
        
        queue = deque([(beginWord, 1)])
        
        while queue:
            word, length = queue.popleft()
            
            if word == endWord:
                return length
            
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + ch + word[i+1:]
                    
                    if newWord in wordSet:
                        queue.append((newWord, length + 1))
                        wordSet.remove(newWord)
        
        return 0