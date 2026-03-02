T = int(input())
for tc in range(1, T+1):

    N = int(input())

    grid = [list(input().strip()) for _ in range(N)]

    # [런타임오류: 제미나이 사용]
    # 델타 탐색인데 상하좌우가 아니라
    # 가로, 세로, 우하 대각선, 좌하 대각선
    # 오목은 이 4방향이면 충분
    dr = [0, 1, 1, 1]
    dc = [1, 0, 1, -1]

    count = 0

    result = "NO"

    for r in range(N):
        for c in range(N):
            if grid[r][c] == 'o':

                for k in range(4):
                    count = 1

                    for j in range(1, 5):
                        nr = r + dr[k]*j
                        nc = c + dc[k]*j

                        if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 'o':
                            count += 1
                        else:
                            break

                    if count >= 5:
                        result = "YES"
                        break

                if result == "YES":
                    break

            if result == "YES":
                break

    print(f"#{tc} {result}")