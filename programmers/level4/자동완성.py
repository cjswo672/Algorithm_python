class Trie:
    def __init__(self):
        self.children = dict()
        self.has_child = self.terminate = False


def solution(words):
    words.sort()
    answer = min(equal_length(words[0], words[1]) + 1, len(words[0]))
    for i in range(1, len(words) - 1):
        prev, next = words[i - 1], words[i + 1]
        answer += min(max(equal_length(prev, words[i]), equal_length(next, words[i])) + 1, len(words[i]))
    answer += min(equal_length(words[-2], words[-1]) + 1, len(words[-1]))
    return answer


def equal_length(word1, word2):
    for i, (ch1, ch2) in enumerate(zip(word1, word2)):
        if ch1 != ch2: return i
    return min(len(word1), len(word2))


def solution2(words):
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