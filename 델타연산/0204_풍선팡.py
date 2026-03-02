T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_p = 0

    # 상하좌우 델타
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(N):
        for j in range(M):
            cnt = matrix[i][j]

            # 현재 위치 꽃가루 수만큼 뻗어나감
            k = matrix[i][j]

            for d in range(4):
                for dist in range(1, k+1):   # 거리 변수 이름 변경 (헷갈리지 않게)
                    nr = i + dr[d] * dist   # 현재 행 i 사용
                    nc = j + dc[d] * dist   # 현재 열 j 사용

                    if 0 <= nr < N and 0 <= nc < M:
                        cnt += matrix[nr][nc]

            if max_p < cnt:
                max_p = cnt

    print(f"#{tc} {max_p}")