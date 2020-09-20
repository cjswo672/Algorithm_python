import heapq

def solution(n, s, a, b, fares):
    answer = 0
    # 최대금액: s -> a, s -> B (다익스트라 했을 시)
    # 102
    # [s -> x(경유) -> a] + [s -> x(경유) -> b] - [s -> x] < 최대금액

    # 1. S에 대해 다익스트라.
    # 2. 각 지점에 대해 A와 B 지점으로 가는 최소 비용 구하기
    # 3. 최대금액 저장: 1[a] + 1[b]
    # 4. 결과 비교: 1[x] + x[a] + x[b] < 3. => 결과 변경

    q = []
    adj = [[] for _ in range(n)]
    visit = [False] * n
    dist = [[987654321 for _ in range(n)] for _ in range(n)]
    
    for f in fares: 
        adj[f[0] - 1].append([f[2], f[1] - 1])
        adj[f[1] - 1].append([f[2], f[0] - 1])
    
    for i in range(n):
        dist[i] = dijstra(n, i, fares, dist, adj)

    ans = dist[s - 1][a - 1] + dist[s - 1][b - 1]
    for i in range(n):
        ans = min(ans, dist[s - 1][i] + dist[i][a - 1] + dist[i][b - 1])
    return ans

def dijstra(n, s, fares, dist, adj):
    q = []
    visit = [False] * n
    dist = dist[s]
    
    dist[s] = 0
    heapq.heappush(q, [0, s])

    while q:
        w, v = heapq.heappop(q)
        if visit[v]: continue
        visit[v] = True
        for i in adj[v]:
            nv = i[1]
            nw = i[0] + dist[v]
            if dist[nv] > nw:
                dist[nv] = nw
                heapq.heappush(q, [nw, nv])
    return dist

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))