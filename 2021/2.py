from collections import defaultdict, Counter

def solution(orders, course):
    d = defaultdict(int)
    answer = []
    for i in range(len(orders)):
        for j in range(len(orders)):
            if i == j: continue
            s = set(orders[i]) & set(orders[j])
            if len(s) < 2: continue
            
            for tmp in get_candidates(sorted(list(s))):
                if tmp in d: d[tmp] += 1
                else: d[tmp] = 1
                
    maximum = [0] * (max(course) + 1)
    for k in d:
        if len(k) in course:
            maximum[len(k)] = max(maximum[len(k)], d[k])
    for k in d:
        if len(k) in course and maximum[len(k)] == d[k]:
            answer.append(k)
    return sorted(answer)

def get_candidates(s):
    if len(s) == 2: return [''.join(s)]
    res = []
    for i in range(1 << len(s)):
        if bin(i).count('1') >= 2:
            tmp = ''
            for j in range(len(s)):
                if 1 << j & i:
                    tmp += s[j]
            res.append(tmp)
    return res

print(solution(	["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))