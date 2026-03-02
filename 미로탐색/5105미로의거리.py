# 상하좌우 델타
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):

    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    visited = [[0]*N for _ in range(N)]

    # 시작점 찾기
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                sr, sc = r, c

    # 큐 만들기 (리스트)
    queue = []
    queue.append((sr, sc))

    visited[sr][sc] = 1   # 거리 1부터 시작

    result = 0

    # BFS 시작
    while queue:
        r, c = queue.pop(0)

        # 도착점이면 종료
        if maze[r][c] == 3:
            result = visited[r][c] - 2
            break

        # 4방향 탐색
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < N:
                if maze[nr][nc] != 1 and visited[nr][nc] == 0:
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append((nr, nc))

    print(f"#{tc} {result}")