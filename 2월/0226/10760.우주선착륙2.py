# 테스트 케이스
T = int(input())
for tc in range(1, T+1):

    # N*M
    N, M = map(int, input().split())

    # 지도
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 착륙 지점 중심으로 주변 8개 대상
    # 착륙지점보다 높이가 낮은 구역은 사진 찍기 가능
    # 사진 찍을 수 있는 방향이 4방향 이상
    # 즉 중앙보다 낮은 지역이 4곳 이상이면 개수 센다는 의미인듯

    # 델타인데 8방향으로(상하좌우대각선)
    dr = [-1,1,0,0,-1,-1,1,1]
    dc = [0,0,-1,1,-1,1,-1,1]

    # 문제에서 원하는 답: 4곳 이상인 곳이 총 개수
    answer = 0

    for r in range(N):
        for c in range(M):
            height = grid[r][c] # 내가 지금 있는 칸의 높이
            # 나보다 낮은 칸
            lower_count = 0

            for i in range(8):
                nr = r + dr[i]
                nc = c + dc[i]

                # 범위
                if 0 <= nr < N and 0 <= nc < M:
                    if grid[nr][nc] < height:
                        lower_count += 1

            # 8방향 조사 후, 낮은 곳 4개 이상인 곳들 개수
            if lower_count >= 4:
                answer += 1


    print(f"#{tc} {answer}")