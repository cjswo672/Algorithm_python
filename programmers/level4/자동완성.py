class Trie:
    def __init__(self):
        self.children = dict()
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
    for i, ch in enumerate(word):
        if not runner.children[ch].has_child:
            return i + 1
        runner = runner.children[ch]
    return len(word)


def get_tries(root, word):
    runner = root
    for ch in word:
        if ch not in runner.children:
            runner.children[ch] = Trie()
        else:
            runner.children[ch].has_child = True
        runner = runner.children[ch]
    runner.terminate = True


print(solution(["go","gone","guild"]))
print(solution(["abc","def","ghi","jklm"]))
print(solution(["word","war","warrior","world"]))