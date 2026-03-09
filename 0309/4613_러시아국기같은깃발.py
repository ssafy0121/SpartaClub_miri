# 이 문제는 강사님께 배우고 싶습니다.


# hint) 쉬운 당근 포장 ?!

# 깃발 N행, M열
# 위에서 몇 줄(한 줄 이상)은 모두 흰색으로 칠해져 있어야 한다.
# 다음 몇 줄(한 줄 이상)은 모두 파란색으로 칠해져 있어야 한다.
# 나머지 줄(한 줄 이상)은 모두 빨간색으로 칠해져 있어야 한다.

T = int(input())

for tr in range(1, T + 1):

    N, M = map(int, input().split())

    flag = list(map(input().strip()))

# ‘W’는 흰색, ‘B’는 파란색, ‘R’은 빨간색을 의미한다.


    for i in range(N-2):

        for j in range(i+1, N-1):
