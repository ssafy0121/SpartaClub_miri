T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 격자판 정보 입력
    area = [list(map(int, input().split())) for _ in range(N)]

    max_flies = 0

    # 중심점 (i, j) 이동
    for i in range(N):
        for j in range(N):

            # 십자가 모양 (+) 합계
            # dr, dc로 상하좌우 표현 (방향 배열)
            dr_plus = [-1, 1, 0, 0]
            dc_plus = [0, 0, -1, 1]

            # 중심값 초기화
            sum_plus = area[i][j]

            # 십자가 4방향으로 M-1 칸씩 뻗어나가기
            for k in range(4):
                for dist in range(1, M):
                    ni = i + dr_plus[k] * dist
                    nj = j + dc_plus[k] * dist

                    # 경계 체크: 도화지 안쪽에 있을 때만 합산
                    if 0 <= ni < N and 0 <= nj < N:
                        sum_plus += area[ni][nj]

            # X자 모양 (×) 합계
            dr_cross = [-1, -1, 1, 1]
            dc_cross = [-1, 1, -1, 1]

            # 중심값 초기화
            sum_cross = area[i][j]

            # X자 4방향으로 M-1 칸씩 뻗어나가기
            for k in range(4):
                for dist in range(1, M):
                    ni = i + dr_cross[k] * dist
                    nj = j + dc_cross[k] * dist

                    # 경계 체크
                    if 0 <= ni < N and 0 <= nj < N:
                        sum_cross += area[ni][nj]

            # 3. 최댓값 갱신: 두 모양 중 더 큰 값
            if sum_plus > max_flies:
                max_flies = sum_plus
            if sum_cross > max_flies:
                max_flies = sum_cross

    print(f"#{tc} {max_flies}")