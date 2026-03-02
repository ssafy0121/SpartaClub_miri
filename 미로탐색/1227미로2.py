# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, 11):

    input()   # 테스트케이스 번호 버리기

    N = 100
    maze = [list(map(int, input())) for _ in range(N)]

    visited = [[0]*N for _ in range(N)]

    # 시작점 찾기
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                sr, sc = r, c

    stack = []
    stack.append((sr, sc))
    visited[sr][sc] = 1

    result = 0

    while stack:
        r, c = stack.pop()

        if maze[r][c] == 3:
            result = 1
            break

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < N:
                if maze[nr][nc] != 1 and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    stack.append((nr, nc))

    print(f"#{tc} {result}")