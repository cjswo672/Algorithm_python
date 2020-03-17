def solution(n, build_frame):
    answer = []
    frame = [[False] * (n + 1) for _ in range(n + 1)]
    pillar = [[False] * (n + 1) for _ in range(n + 1)]
    for cmd in build_frame:
        if cmd[2]:
            frame[cmd[1]][cmd[0]] = True if cmd[3] else False
        else:
            pillar[cmd[1]][cmd[0]] = True if cmd[3] else False

        if not (check_frame(frame, pillar) and check_pillar(frame, pillar)):
            if cmd[2]: frame[cmd[1]][cmd[0]] ^= frame[cmd[1]][cmd[0]]
            else: pillar[cmd[1]][cmd[0]] ^= pillar[cmd[1]][cmd[0]]

    for i in range(n + 1):
        for j in range(n + 1):
            if pillar[i][j]: answer.append([j, i, 0])
            if frame[i][j]: answer.append([j, i, 1])

    return sorted(answer)


# 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
def check_frame(frame, pillar):
    for i in range(len(frame)):
        for j in range(len(frame)):
            if frame[i][j]:
                # 한쪽 끝 부분이 기둥 위에 있어야한다.
                # 왼쪽 끝 부분이 기둥 위에 있어야한다.
                if i > 0 and pillar[i - 1][j]:
                    continue
                # 오른쪽 끝 부분이 기둥 위에 있어야한다.
                if i > 0 and j < len(pillar[0]) - 1 and pillar[i - 1][j + 1]:
                    continue
                # 양쪽 끝 부분이 다른 보와 연결되어 있어야 한다
                if (j > 0 and frame[i][j - 1]) and (j < len(frame) - 1 and frame[i][j + 1]):
                    continue
                return False
    return True


# 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
def check_pillar(frame, pillar):
    for i in range(len(frame)):
        for j in range(len(frame)):
            if pillar[i][j]:
                # 바닥 위에 있어야 한다
                if i == 0: continue
                # 보의 한쪽 끝 부분 위에 있어야 한다
                if frame[i][j] or j > 0 and frame[i][j - 1]: continue
                # 다른 기둥 위에 있어야 한다
                if i > 0 and pillar[i - 1][j]: continue
                return False
    return True


print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
