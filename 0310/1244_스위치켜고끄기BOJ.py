# ‘1’은 스위치가 켜져 있음을, ‘0’은 꺼져 있음
# 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다.
# 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꾼다.

# 첫째 줄에는 스위치 개수가 주어진다.
# 둘째 줄에는 각 스위치의 상태가 주어진다.
# 셋째 줄에는 학생수가 주어진다.
# 넷째 줄부터 마지막 줄까지 한 줄에 한 학생의 성별, 학생이 받은 수가 주어진다. 남학생은 1로, 여학생은 2로 표시

# 입력값
'''
8
0 1 0 1 0 0 0 1
2
1 3
2 3
'''

N = int(input())
# 입력: 8

switch = list(map(int, input().split()))
# 입력: 0 1 0 1 0 0 0 1

student = int(input())
# 입력: 2


for _ in range(student):
    gender, num = map(int, input().split())

    # 첫 번째 학생 입력
    # 1 3
    #
    # gender = 1 (남학생)
    # num = 3

    # 남학생
    if gender == 1:
        # 인덱스는 0부터 시작이니까 num-1
        for i in range(num-1, N, num):
            # range(2, 8, 3)

            # 1 -> 0
            # 0 -> 1

            # i = 2
            switch[i] = 1 - switch[i]

    # 여학생
    else:
        center = num - 1
        switch[center] = 1 -switch[center]

        # 좌우 확장 거리
        d = 1

        # 얼마나 확장 되는 지 모르니까 while
        while True:
            left = center - d
            right = center + d

            # 범위를 벗어나면 종료
            if left < 0 or right >= N:
                break

            # 좌우 값이 다르면 종료
            if switch[left] != switch[right]:
                break

            # 좌우 값이 같으면 둘 다 뒤집기
            switch[left] = 1 - switch[left]
            switch[right] = 1 - switch[right]

            d += 1

for i in range(N):

    print(switch[i], end=' ')

    # 스위치의 상태를 1번 스위치에서 시작하여 마지막 스위치까지 한 줄에 20개씩 출력한다.
    if (i+1) % 20 == 0:
        print()