class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        L = len(beginWord)

        pattern_map = defaultdict(list)
        for word in wordSet:
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_map[pattern].append(word)

        parents = defaultdict(set)
        level = {beginWord}
        found = False

        while level and not found:
            next_level = set()
            wordSet -= level

            for word in level:
                for i in range(L):
                    pattern = word[:i] + "*" + word[i+1:]
                    for nei in pattern_map[pattern]:
                        if nei in wordSet:
                            next_level.add(nei)
                            parents[nei].add(word)
                            if nei == endWord:
                                found = True

            level = next_level

        if not found:
            return []

        res = []

        def dfs(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            for p in parents[word]:
                dfs(p, path + [p])

        dfs(endWord, [endWord])
        return res