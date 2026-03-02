T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    max_p = 0

    for i in range(N):
        for j in range(M):
            cnt = matrix[i][j]

            for d in range(4):
                nr = i + dr[d]
                nc = j + dc[d]
                if 0 <= nr < N and 0 <= nc < M:
                    cnt += matrix[nr][nc]

            if max_p < cnt:
                max_p = cnt

    print(f"#{tc} {max_p}")