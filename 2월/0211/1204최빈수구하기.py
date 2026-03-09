# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
T = int(input())

# 테스트 케이스 T 만큼 반복
for tc in range(1, T+1):
    # 각 테스트 케이스(출력용)
    # 이거 안 하면 아래처럼 나옴
    #1 1
    #2 71
    #3 2
    #4 76
    tc = int(input())

    # 입력받는 학생 점수
    Numbers = list(map(int, input().split()))

    # 점수 0 ~ 100 (등장 횟수를 저장할 카운팅 배열)
    cnt = [0] * 101

    # 가장 많이 나오는 횟수
    max_cnt = 0

    # 최빈수 # 우리가 찾는 것
    mode = 0

    # 카운팅 하기
    for num in Numbers:
        cnt[num] += 1

    # 최빈수 찾기
    for i in range(len(cnt)):
        if cnt[i] >= max_cnt:
            max_cnt = cnt[i]
            # 등장 횟수를 최빈수로 저장하기
            mode = i

    # 부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력한다.
    print(f"#{tc} {mode}")
