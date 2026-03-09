# 첫 줄에 테스트 케이스 개수 T가 주어진다.
T = int(input())
for tc in range(1, T+1):
# 다음 줄부터 테스트케이스의 첫 줄에 칠할 영역의 개수 N이 주어진다.
# 다음 줄에 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color가 주어진다.
    # N개의 영역
    N = int(input())

    # 10*10 격자
    paper = [[0]*10 for _ in range(10)]

    # 우리가 원하는 답
    count = 0

    for _ in range(N):
        # 행,열,행,열,색
        r1, c1, r2, c2, color  = map(int, input().split())

        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                paper[r][c] += color
                # color = 1 (빨강), color = 2 (파랑)
                # 숫자 1에 2가 겹치면 보라색이니까 3이지.
                if paper[r][c] == 3:
                    # 보라색
                    count += 1


    # 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
    print(f"#{tc} {count}")