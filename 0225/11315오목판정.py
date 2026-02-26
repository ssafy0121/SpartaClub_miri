#테스트 케이스
T = int(input())
for tc in range(1, T + 1):

# N*N판
    N = int(input())

    # [런타임오류: 제미나이 사용]
    # 정수(int)로 변환하지 않고 문자열 그대로 리스트로 만듭니다.
    # 'o'나 '.'은 숫자가 아니기 때문에 map(int, ...)를 쓰면 에러가 납니다.
    board = [list(input().strip()) for _ in range(N)]

    # [런타임오류: 제미나이 사용]
    #새로운 방향을 검사할 때마다 다시 1부터 시작해야하니 이거 설정 X
    # count = 0

    # NO로 하고 시작
    result = "NO"

    # [런타임오류: 제미나이 사용]
    # 델타 탐색인데 상하좌우가 아니라
    # 가로, 세로, 우하 대각선, 좌하 대각선
    dr = [0, 1, 1, 1]
    dc = [1, 0, 1, -1]

    # 모든 칸 하나씩 검사
    for r in range(N):  # 모든 행 검사
        for c in range(N):  # 모든 열 검사
            # 현재 칸에 돌(o)이 있는 경우에만 체크 시작
            if board[r][c] == 'o':

                # 4방향으로 5개가 연속된다면 1
                for i in range(4):
                    count = 1

                    # 해당 방향으로 4칸 더 가보기 (나 포함 5개 확인)
                    for k in range(1, 5):
                        nr = r + dr[i] * k
                        nc = c + dc[i] * k

                        # 범위와 연속해서 'o'이 있다면
                        if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 'o':
                            count += 1
                        else:
                            break

                    #[런타임오류: 제미나이]
                    # 아래 부분 들여쓰기 틀렸었음
                    if count >= 5:
                        result = "YES"
                        break

            if result == "YES":
                break

        if result == "YES":
            break


    print(f"#{tc} {result}")
