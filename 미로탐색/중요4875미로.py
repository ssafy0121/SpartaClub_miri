# 상하좌우
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

    # 스택 만들기 (DFS)
    stack = []
    stack.append((sr, sc))
    visited[sr][sc] = 1

    result = 0  # 도착 못 하면 0

    # DFS 시작
    while stack:
        r, c = stack.pop()   # 뒤에서 꺼냄 (DFS)

        # 도착점이면 성공
        if maze[r][c] == 3:
            result = 1
            break

        # 4방향 탐색
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            # 범위 안이고
            if 0 <= nr < N and 0 <= nc < N:

                # 길이고 방문 안 했으면
                if maze[nr][nc] != 1 and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    stack.append((nr, nc))

    print(f"#{tc} {result}")