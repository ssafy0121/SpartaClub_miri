# 테스트 케이스
T = int(input())
for tc in range(1, T+1):

    # N*N개 칸
    N = int(input())

    #0: 빈칸, 1: 벽, 2: 괴물
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 괴물 위치 리스트
    monster = []
    for r in range(N):
        for c in range(N):
            if grid[r][c] == 2:
                monster.append((r,c))

    # 4방향 광선
    for r, c in monster:
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            # 격자판 범위 안
            while 0 <= nr < N and 0 <= nc < N and grid[nr][nc] != 1:
                # 만약 빈칸(0)이라면 닿았다고 표시 (-1)
                # 괴물(2)는 무시
                if grid[nr][nc] == 0:
                    grid[nr][nc] = -1

                    nr += dr[i]
                    nc += dc[i]

    # 안전한 방 개수 세기
    count = 0
    for r in range(N):
        for c in range(N):
            if grid[r][c] == 0:
                count += 1

    print(f"#{tc} {count}")