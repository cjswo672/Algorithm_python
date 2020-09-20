from collections import defaultdict

ans = 987654321
chs = defaultdict(list)
def solution(board, r, c):
    answer = 0
    visit = [False] * 7
    for r1 in range(4):
        for c1 in range(4):
            if board[r1][c1]:
                chs[board[r1][c1]].append([r1, c1])
    move(board, visit, len(chs), [0, 0], [r, c], 0)
    return ans

def move(board, visit, depth, delete, pos, cost):
    if depth == 0:
        global ans
        ans = min(ans, cost)
        return

    if delete[0]:
        visit[delete[0]] = True
        next = chs[delete[0]][delete[1]]
        tmp = board[next[0]][next[1]]
        board[next[0]][next[1]] = 0

        next_cost = cost + get_distance(board, pos, chs[delete[0]][delete[1]]) + 1
        move(board, visit, depth - 1, [0, 0], chs[delete[0]][delete[1]], next_cost)

        board[next[0]][next[1]] = tmp
        visit[delete[0]] = False
    else:
        for i in chs:
            if visit[i]: continue
            next_cost_0 = get_distance(board, pos, chs[i][0])
            next_cost_1 = get_distance(board, pos, chs[i][1])
            
            if next_cost_0 < next_cost_1:
                tmp = board[chs[i][0][0]][chs[i][0][1]]
                board[chs[i][0][0]][chs[i][0][1]] = 0
                move(board, visit, depth, [i, 1], chs[i][0], cost + next_cost_0 + 1)
                board[chs[i][0][0]][chs[i][0][1]] = tmp
            else:
                tmp = board[chs[i][1][0]][chs[i][1][1]]
                board[chs[i][1][0]][chs[i][1][1]] = 0
                move(board, visit, depth, [i, 0], chs[i][1], cost + next_cost_1 + 1)
                board[chs[i][1][0]][chs[i][1][1]] = tmp
    return

def get_distance(board, p1, p2):
    return get_distance2(board, p1, p2, [[False for _ in range(4)] for _ in range(4)])

# p1에서 p2로 가는 비용
def get_distance2(board, p1, p2, visit):
    if p1[0] < 0 or p1[1] < 0 or p1[0] > 3 or p1[1] > 3: return 987654321
    if p1 == p2: return 0
    if visit[p1[0]][p1[1]]: return 987654321
    visit[p1[0]][p1[1]] = True
    
    res = 987654321
    if abs(p1[0] - p2[0]):
        if p1[0] < p2[0]: # d
            res = min(res, get_distance2(board, [p1[0] + 1, p1[1]], p2, visit) + 1)

            tmp = p1[0] + 1
            while tmp < 3 and not board[tmp][p1[1]]: tmp += 1
            res = min(res, get_distance2(board, [tmp, p1[1]], p2, visit) + 1)
        else: # u
            res = min(res, get_distance2(board, [p1[0] - 1, p1[1]], p2, visit) + 1)

            tmp = p1[0] - 1
            while tmp > 0 and not board[tmp][p1[1]]: tmp -= 1
            res = min(res, get_distance2(board, [tmp, p1[1]], p2, visit) + 1)
    
    if abs(p1[1] - p2[1]):
        if p1[1] > p2[1]:  # l
            res = min(res, get_distance2(board, [p1[0], p1[1] - 1], p2, visit) + 1)
            
            tmp = p1[1] - 1
            while tmp > 0 and not board[p1[0]][tmp]: tmp -= 1
            res = min(res, get_distance2(board, [p1[0], tmp], p2, visit) + 1)
        else: # r
            res = min(res, get_distance2(board, [p1[0], p1[1] + 1], p2, visit) + 1)

            tmp = p1[1] + 1
            while tmp < 3 and not board[p1[0]][tmp]: tmp += 1
            res = min(res, get_distance2(board, [p1[0], tmp], p2, visit) + 1)

    visit[p1[0]][p1[1]] = False
    return res

print(solution([
    [6, 3, 5, 2], 
    [0, 4, 1, 0], 
    [5, 1, 0, 4], 
    [0, 2, 6, 3]], 0, 1))