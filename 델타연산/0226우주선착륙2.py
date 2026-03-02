T = int(input())
for tc in range(1, T + 1):

    N, M = map(int, input().split())

    grid = [list(map(int, input().split())) for _ in range(N)]

    answer = 0

    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, -1, 1]

    for r in range(N):
        for c in range(M):
            height = grid[r][c]
            count = 0

            for k in range(8):
                nr = r + dr[k]
                nc = c + dc[k]

                if 0 <= nr < N and 0 <= nc < M:
                    if grid[nr][nc] < height:
                        count += 1

            if count >= 4:
                answer += 1

    print(f"#{tc} {answer}")
