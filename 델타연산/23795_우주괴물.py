# T: 테스트 케이스 개수
T = int(input())

for tc in range(1, T + 1):
    # N: 격자 크기, M: 레이저 사거리
    N, M = map(int, input().split())
    # 격자 정보 입력
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 1. 우주 괴물(2)의 위치 찾기
    r, c = -1, -1
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 2:
                r, c = i, j
                break
        if r != -1: break

    # 2. 델타 배열 설정 (상, 하, 좌, 우)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    total_cells = 0  # 레이저가 닿은 칸 수

    # 3. 4방향으로 레이저 발사
    for i in range(4):
        # 사거리 M만큼 한 칸씩 뻗어나감
        for dist in range(1, M + 1):
            nr = r + dr[i] * dist
            nc = c + dc[i] * dist

            # 격자 범위 안에 있는지 확인 (경계 체크)
            if 0 <= nr < N and 0 <= nc < N:
                # 벽(1)을 만나면 이 방향은 레이저가 막힘! -> break
                if grid[nr][nc] == 1:
                    break
                # 빈칸(0)이면 카운트하고 계속 전진
                elif grid[nr][nc] == 0:
                    total_cells += 1
            else:
                # 격자 밖으로 나가면 이 방향은 종료
                break

    print(f"#{tc} {total_cells}")