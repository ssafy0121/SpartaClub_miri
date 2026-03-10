T = int(input())
for tc in range(1, T+1):

    N,M = map(int, input().split())

    flag = [input() for _ in range(N)]

    # 정답: 최소 색칠 횟수(아주 큰 값으로 시작)
    answer = 10000000000

    # 첫 줄
    for i in range(N-2):
        for j in range(i+1, N-1):

            count = 0

            # 인덱스 0 ~ i까지
            for r in range(0, i+1):
                for c in range(M):

                    # 현재 칸이 W가 아니면
                    if flag[r][c] != 'W':
                        count += 1

            # 인덱스 i+1 ~ j
            for r in range(i+1, j+1):
                for c in range(M):
                    if flag[r][c] != 'B':
                        count += 1

            # j+1 ~ N-1
            for r in range(j+1, N):
                for c in range(M):
                    if flag[r][c] != 'R':
                        count += 1

            # 현재 경우가 더 작으면 정답 갱신
            if count < answer:
                answer = count



    print(f"#{tc} {answer}")