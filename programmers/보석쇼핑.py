def solution(gems):
    gem_count, l = len(set(gems)), -1
    candidates, d = [], dict()

    for r, gem in enumerate(gems):
        if d.get(gem): d[gem] += 1
        else: d[gem] = 1

        if len(d) == gem_count:
            while l <= r and d[gems[l]] > 0:
                l += 1
                d[gems[l]] -= 1
            candidates.append([l + 1, r + 1])
            d.pop(gems[l])
            
    candidates.sort(key=lambda x: x[1] - x[0])
    return candidates[0]
    
# sol#1 -> o(n)
# 1. dict에 원소들을 넣는다. -> o(1)
# 2. len(s) == gem_count가 됐을 때 정지한다.(r) -> o(n)
# 3. dict의 원소들 중 하나라도 1 미만이 되기 전까지 (l)을 1씩 더하며 dict에서 1씩 제거한다. -> o(n + 1)
# 4. 1.을 반복한다.(dict에서 마지막 아이템(l) 제거) -> o(1)

# sol#2 (이분 탐색) -> o(n log n)
# 1. l=gem_count, r=len(gems)로 시작한다.
# 2. i ~ i + m에서 원소의 갯수를 구한다. (원소의 종류가 gem_count와 같으면 시작 idx 저장 후 종료)
# 3-1. 2.가 gem_count보다 작으면 l = m + 1
# 3-2. 2.가 gem_count보다 크거나 같으면 r = m - 1, ans = min(ans, m)

print(solution("a b a a c d b".split()))