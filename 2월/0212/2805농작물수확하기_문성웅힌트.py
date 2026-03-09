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

# 문성웅 힌트
# #1. 홀수니까 중앙을 기준으로 상단/중앙/하단 나누어서 계산 후 합산
    # 중앙
    mid = N // 2

# 2. 상단의 경우 최고위치(1행, 값 한개인 곳) 부터 반복문을 통해 시작점과 끝 점 계산.
# 3. 중앙을 center 라 하면 첫줄은 range(center, center) 가 되어야함.
#  - 두번째 줄은 range(center -1, center + 1 +1) range의 끝 점은 포함하지 않으므로 하나 더 늘려줘야 함.
#  - 위와 같은 방식으로 아래로 내려 갈수록  range(center -2, center + 2 +1) >> range(center -3, center + 3 +1) 으로 진행함
#  - 최종 위치는 중앙 행 한 칸 위 까지 계산 인덱스 번호 N//2 -1 까지만 계산하여야 한다.
    for i in range(mid):
        start = mid - i
        end = mid + i

#  - 해당 range 내부의 값은 반복문을 통해 변경을 해보자! (따로 start, end 와 같이 변수를 지정하여 range(start, end)를 하면 식이 깔끔해짐)
        # range의 끝 점은 포함하지 않으므로 + 1  # 이거 조심하자!!!
        for j in range(start, end+1):
            total += farm[i][j]

# 4. 중앙 행 따로 반복문 제작하여 합을 구한다.
    for j in range(N):
        total += farm[mid][j]
# 5. 하단의 경우 밑바닥 부터 출발하여 상단과 같은 방식으로 계산
# 6. 중앙 행 한 칸 아래까지 합산하며 진행하면 된다.
# 중앙 다음(mid+1)부터 끝까지 내려가는 게 편함 # 챗GPT
    for i in range(mid+1, N):
        # 중앙에서 멀어질수록(i-mid) 범위가 다시 좁아짐
        # 아래쪽 첫 줄(mid+1)은 한 칸 줄어든 mid-1 ~ mid+1 범위가 된다 # 챗GPT
        offset = i-mid
        start = offset
        end = (N-1) - offset
        for j in range(start, end+1):
            total += farm[i][j]
# 7. 상단, 중앙, 하단 의 합을 모두 합하여 출력하면 된다. 혹은 누적 합을 통해 하나의 변수에 값을 누적하자!
    print(f"#{tc} {total}")