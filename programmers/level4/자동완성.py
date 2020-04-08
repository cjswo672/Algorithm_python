class Trie:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.has_child = self.terminate = False


def solution(words):
    root = Trie()
    for word in words:
        get_tries(root, word)
    answer = 0
    for word in words:
        answer += find(root, word)
    return answer


def find(root, word):
    runner = root
    for i in range(len(word)):
        n = ord(word[i]) - 97
        if not runner.children[n].has_child:
            return i + 1
        runner = runner.children[n]
    return len(word)


def get_tries(root, word):
    runner = root
    for ch in word:
        n = ord(ch) - 97
        if runner.children[n] is None:
            runner.children[n] = Trie()
        else:
            runner.children[n].has_child = True
        runner = runner.children[n]
    runner.terminate = True


print(solution(["go","gone","guild"]))
print(solution(["abc","def","ghi","jklm"]))
print(solution(["word","war","warrior","world"]))