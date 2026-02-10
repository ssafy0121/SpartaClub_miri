# 가장 첫 줄에 테스트 케이스 개수 T가 주어지고
T = int(input())
# 테스트 케이스
for tc in range(1, T+1):

    # 주어지는 숫자들
    Numbers = map(int, input().split())

    # 홀수만 더한 값 출력
    # 더하기 total
    total = 0
    # 반복문
    for num in Numbers:
        # 홀수
        if num % 2 == 1:
            # 홀수면 더하기
            total += num


    # 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
    print(f"#{tc} {total}")