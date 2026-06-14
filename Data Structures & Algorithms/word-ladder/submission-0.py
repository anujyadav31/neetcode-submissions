class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)

        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0
'''
#from collections import defaultdict, deque
        if endWord not in wordList:
            return 0

        nei = defaultdict(list)
        print(f"nei = {nei}")

        print(f"wordList = {wordList}")
        # Add beginWord so its patterns are also generated
        wordList.append(beginWord)
        print(f"wordList = {wordList}")
        print("...........................................................................")

        for word in wordList:
            for j in range(len(word)):
                print(f"word = {word}")
                pattern = word[:j] + "*" + word[j + 1:]
                print(f"pattern = {pattern}")
                nei[pattern].append(word)
                print(f"nei[{pattern}] = {nei[pattern]}")
                print("..........................")

        print("...........................................................................")
        visit = {beginWord}
        print(f"visit = {visit}")
        q = deque([beginWord])
        print(f"q = {q}")
        print("...........................................................................")
        res = 1
        print(res)
        print("..........................")

        while q:
            print(f"q = {q}")
            for _ in range(len(q)):
                word = q.popleft()
                print(f"word = {word}")

                if word == endWord:
                    print(f"word == endWord = {word == endWord}, res = {res}")
                    return res

                for j in range(len(word)):
                    print(f"j = {j}")
                    pattern = word[:j] + "*" + word[j + 1:]
                    print(f"pattern = {pattern}")

                    for neiWord in nei[pattern]:
                        print(f"neiWord = {neiWord} in nei[{pattern}] = {nei[pattern]}")
                        if neiWord not in visit:
                            print(f"{neiWord} not in visit")
                            print(f"visit = {visit}")
                            visit.add(neiWord)
                            print(f"visit.add({neiWord}) = {visit}")
                            print(f"q = {q}")
                            q.append(neiWord)
                            print(f"q.append({neiWord}) = {q}")
            print("..........................")

            res += 1
            print(res)
            print("..........................")

        return 0


# Input
beginWord = "cat"
endWord = "sag"
wordList = ["bat", "bag", "sag", "dag", "dot"]

# Run
sol = Solution()
result = sol.ladderLength(beginWord, endWord, wordList)

#print("Shortest transformation length:", result)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
'''