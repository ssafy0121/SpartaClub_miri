# 상하좌우 델타
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, 11):   # 10개 고정

    input()  # 테스트케이스 번호 입력 (버려도 됨)

    N = 16
    maze = [list(map(int, input())) for _ in range(N)]

    visited = [[0]*N for _ in range(N)]

    # 시작점 찾기
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                sr, sc = r, c

    # DFS 스택
    stack = []
    stack.append((sr, sc))
    visited[sr][sc] = 1

    result = 0

    # 암기하자!!!
    # 거리 구하라 -> BFS
    # 가능 여부 -> DFS

    # DFS 탐색
    while stack:
        r, c = stack.pop()

        # 도착점이면 성공
        if maze[r][c] == 3:
            result = 1
            break

        # 4방향 탐색
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            # 범위 체크
            if 0 <= nr < N and 0 <= nc < N:

                # 길이고 방문 안 했으면
                if maze[nr][nc] != 1 and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    stack.append((nr, nc))

    print(f"#{tc} {result}")