# 테스트 케이스 T
T = int(input())
for tc in range(1, T+1):

    # 한 줄에 세 숫자 A B C 를 입력받는다
    # map(int, ...) → 문자열을 숫자로 바꿔줌
    # 입력값이 3 2 1 이렇게 오니까 split()
    A, B, C = map(int, input().split())

    # 목표는 A < B < C 이고 모두 1 이상이어야 함
    # z는 최대한 크게
    z = C

    # y는 z보다 작아야 함
    y = min(B, z-1)

    # x는 y보다 작아야 함
    x = min(A, y-1)

    # x < y < z 확인
    if x >= 1 and x <y and y < z:
        # 먹은 개수 = 원래 - 남은
        eaten = (A-x) + (B-y) + (C-z)
        print(f"#{tc} {eaten}")
    else:
        # 불가능한 경우
        print(f"#{tc} -1")
