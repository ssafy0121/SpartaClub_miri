# 강사님, 이 문제 명확히 이해가 안 된 부분들 # 표시 했습니다.
# 배움을 주십시오.


# 함수 정의
def path(line, N, X):
    # 주복 방지
    visited = [False] * N

    # 강사님, 여기 AI한테 물어봐도 왜 N-1인지 이해가 안 됩니다.
    # N 해도 0부터 N-1까지 돌지 않나요?
    # 밑에는 AI 설명입니다.
    # range(N) -> i의 마지막은 N-1 -> i+1은 N (에러!)
    # range(N-1) -> i의 마지막은 N-2 -> i+1은 N-1 (마지막 칸 도달, 안전!)
    for i in range(N-1):
        # 높이가 같은 경우 패스
        if line[i] == line[i+1]:
            continue

        # 높이 차이가 1보다 크면 경사로 X
        if abs(line[i] - line[i+1]) > 1:
            return False

        # 내리막길 (경사로)
        if line[i] > line[i+1]:
            for j in range(i+1, i+1+X):
                # 만약 가다가 지도 밖으로 떨어지거나(j >= N)
                # 바닥 높이가 달라서 경사로가 흔들리거나
                # 이미 경사로 스티커가 붙어있으면 X
                if j >= N or line[j] != line[i+1] or visited[j]:
                    return False
                visited[j] = True

        # 오르막길일 경우
        elif line[i] < line[i+1]:

            # 강사님, 이 부분도 범위가
            for j in range(i, i-X, -1):
                # 뒤로 가다가 지도 밖으로 나간다(j < 0),
                # 바닥 높이가 달라서 삐뚤어딘다
                # 이미 스티커가 붙어있다 X
                if j < 0 or line[j] != line[i] or visited[j]:
                    return False
                visited[j] = True

    return True

# 테스트 케이스
T = int(input())
for tc in range(1, T + 1):
    # 경사로 길이 X, 높이 1
    N, X = map(int, input().split())

    # N*N 크기
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 문제에서 원하는 답: 활주로를 건설할 수 있는 경우의 수
    answer = 0

    # 가로
    for r in range(N):
        if path(grid[r], N, X):
            answer += 1

    # 세로
    for c in range(N):
        # 이 부분도 바로 위에 가로처럼 썼다가 AI한테 물었습니다.
        # 강사님께 설명 듣고 확실히 알고 싶습니다.
        # AI 설명: 세로는 세워서 검사
        col_line = [grid[r][c] for r in range(N)]
        if path(col_line, N, X):
            answer += 1


    print(f"#{tc} {answer}")

    

