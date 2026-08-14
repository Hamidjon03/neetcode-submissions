import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        q = deque([beginWord])
        step = 1

        visit = set(wordList)

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for i, char in enumerate(node):
                    characters = string.ascii_lowercase
                    for char in characters:
                        new_word = node[:i] + char + node[i+1:]
                        if new_word == endWord:
                            return step + 1
                        if new_word in visit:
                            q.append(new_word)
                            visit.remove(new_word)
            step += 1
        
        return 0