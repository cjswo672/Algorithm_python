# 못품
def solution(land, P, Q):
    answer = -1
    return answer


# 막 풀기
# min(land) ~ max(land)를 순회하면서 i보다 크면 (land - i) * q, 작으면 (i - land) * p를 더한 값의 최솟값
# 개선: min ~ max 까지 탐색하는게 오래걸림 (각 블록당 범위: 0 ~ 10억)
# 개선: 한 층을 이동할 때 처음부터 계산할 필요 없음.
#       i 층에서 -> i + 1: (i층에 있는 블록 * p - i층의 빈 블록 * q). i - 1: 반대로.
def solution1(land, P, Q):
    land = sum(land, [])
    answer = 987654321987654
    for i in range(min(land), max(land) + 1):
        answer = min(answer, calculate(land, P, Q, i))
    return answer


def solution2(land, P, Q, l, r):
    return 0


def calculate(land, P, Q, v):
    res = 0
    for l in land:
        if v < l: res += (l - v) * Q
        elif v > l: res += (v - l) * P
    return res


print(solution1([[4, 4, 3], [3, 2, 2], [ 2, 1, 0 ]], 5, 3))