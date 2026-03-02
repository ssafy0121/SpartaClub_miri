T = int(input())
for tc in range(1, T+1):

    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 모든 칸 순회
    for r in range(N):
        for c in range(N):

            # 괴물을 만나면
            if grid[r][c] == 2:

                # 4방향으로 광선 쏘기
                for d in range(4):

                    nr = r + dr[d]
                    nc = c + dc[d]

                    # 벽(1)을 만나기 전까지 계속 이동
                    while 0 <= nr < N and 0 <= nc < N and grid[nr][nc] != 1:

                        if grid[nr][nc] == 0:
                            grid[nr][nc] = -1

                        # 다음 칸으로 계속 전진
                        nr += dr[d]
                        nc += dc[d]

    # 안전한 방 세기 (0만 세기)
    count = 0
    for r in range(N):
        for c in range(N):
            if grid[r][c] == 0:
                count += 1

    print(f"#{tc} {count}")