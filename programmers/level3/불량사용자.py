def solution(user_id, banned_id):
    answer = []
    backtracking(0, user_id, banned_id, 0, answer)
    return answer


def backtracking(depth, user_ids, banned_ids, current, ans):
    if depth == len(banned_ids):
        if current in ans: return 0
        ans.append(current)
        return 1

    res = 0
    for i in range(len(user_ids)):
        if current & (1 << i) or not possible(user_ids[i], banned_ids[depth]): continue
        current |= 1 << i
        res += backtracking(depth + 1, user_ids, banned_ids, current, ans)
        current ^= 1 << i
    return res


def possible(user_id, banned_id):
    if len(user_id) != len(banned_id): return False
    for uid, bid in zip(user_id, banned_id):
        if bid != '*' and uid != bid:
            return False
    return True


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]	))
print(solution(	["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
