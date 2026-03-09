# 신민석 강사님
#2차원배열안의 어떤 칸(i,j) i행 j열에서 농작물을 수확하는지 하지 않는지 여부는
#농장의 가운데 좌표 (N//2 , N//2) 에서 가로세로 합쳐서 N//2 칸 이하인지 아닌지를 검사하면 된다.
#모든 위치를 순회하며 농장 가운데 칸과 가로세로 몇칸 떨어져있는지 계산하고, 칸수가 N//2 이하라면 농작물 수확!


# 테스트 케이스
T = int(input())
for tc in range(1, T+1):

    # 농장의 크기 N:     # N*N   # 항상 홀수
    N = int(input())

    # 농장 격자
    farm = []

    # 반복
    for i in range(N):
        # 공백이 없으므로 input()을 바로 list로 감싸야 한 글자씩 쪼개짐
        # row : 가로 줄
        row = list(map(int, input()))
        farm.append(row)

    # 원하는 답
    total = 0

    # 농장의 중앙
    mid = N // 2

    # 농장의 모든 칸 순회 (i 행 j 열)
    for i in range(N):
        for j in range(N):
            # i 행이 중앙에서 얼마나 떨어졌는지 (세로)
            row_d = abs(mid-i)

            # j 열리 중앙과 얼마나 떨어져 있는지 (가로)
            col_d = abs(mid-j)

            # 가로세로 거리의 합이 mid 이하인가
            # 마름모 안에 들어오게끔
            if row_d + col_d <= mid :
                total += farm[i][j]


    print(f"#{tc} {total}")