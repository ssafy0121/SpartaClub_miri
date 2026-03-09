# 10개의 수를 입력 받아
T = int(input())
for tc in range(1, T + 1):
    Numbers = map(int, input().split())

    # 전체 합
    total = sum(Numbers)
    avg = total / 10

    result = int(avg + 0.5)

    # 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
    print(f"#{tc} {result}")
