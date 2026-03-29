class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        l = len(beginWord)
        word_type = defaultdict(list)
        for word in wordList:
            for i in range(l):
                word_type[word[:i] + '*' + word[i + 1:]].append(word)
        
        q = deque()
        q.append((beginWord, 1))
        visited = set()
        visited.add(beginWord)

        while q:
            current_word, step = q.popleft()
            for i in range(l):
                intermediateWord = current_word[:i] + '*' + current_word[i + 1:]
                for new_word in word_type[intermediateWord]:
                    if new_word == endWord:
                        return step + 1
                    if new_word not in visited:
                        visited.add(new_word)
                        q.append((new_word, step + 1))
                word_type[intermediateWord] = []
        return 0

