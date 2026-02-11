# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
T = int(input())
for tc in range(1, T+1):

    # N의 배수 번호인 양을 세기
    # 처음에 map 썼는데.. map은 여러 숫자를 동시에 받을 때 쓰고
    # 지금은 N 하나만 받으니까 int(input()) # 기억하자!
    N = int(input())

    # 첫 번째에는 N번 양을 세고
    # 두 번째에는 2N번 양
    # k번째에는 kN번 양
    K = 1

    # 첫 번째로 N = 1295번 양을 센다. 현재 본 숫자는 1, 2, 5, 9이다.
    # 양을 센다.

    # 0~9 숫자를 담을 바구니
    sheep = set()

    # 반복시작 몇 번을 할 지 모르니 while
    while True:
        # 양들의 번호
        sheep_number = N * K

        # sheep_number이 숫자 상태라 쪼개질 못해서 문자열로 만들어줘야 함
        for s in str(sheep_number):
            sheep.add(s)

        # 10개 다 모았으면 완료!
        if len(sheep) == 10:
            break

        # 아직 다 안 모였으면 다음 배수로 넘어가기
        K += 1

    # 출력
    print(f"#{tc} {sheep_number}")
