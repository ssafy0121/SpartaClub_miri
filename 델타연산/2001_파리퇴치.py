T = int(input())

for tc in range(1, T + 1):
    # N: 전체 영역 크기, M: 파리채 크기
    N, M = map(int, input().split())

    # N x N 크기
    area = [list(map(int, input().split())) for _ in range(N)]

    max_flies = 0  # 가장 많이 잡은 파리 수 저장 변수

    # 1. 파리채의 왼쪽 상단 꼭짓점 (i, j)가 이동할 수 있는 범위 설정
    # 파리채가 영역 밖으로 나가면 안 되므로 N-M+1 까지만 이동
    for i in range(N - M + 1):
        for j in range(N - M + 1):

            # 2. 현재 (i, j) 위치에서 M x M 크기만큼 파리 합계 구하기
            current_sum = 0
            for r in range(i, i + M):  # 파리채의 세로 범위
                for c in range(j, j + M):  # 파리채의 가로 범위
                    current_sum += area[r][c]

            # 3. 최댓값 갱신
            if current_sum > max_flies:
                max_flies = current_sum

    print(f"#{tc} {max_flies}")