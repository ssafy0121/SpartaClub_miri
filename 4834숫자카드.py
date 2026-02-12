# 테스트 케이스 T개
# 테스트 케이스 번호
T = int(input())
for tc in range(1, T+1):

    # 0~9 숫자 카드 N 장 개수를 받음
    N = int(input())

    # 카드 뭉치들을 문자열로 받기 # 예시: 49679
    cards = input()

    # 10칸짜리 장부 만들기
    # 카드 장 수
    count = [0] * 10

    # 카드 뭉치에서 하나씩 꺼내서 장부에 적기
    for i in range(N):
        num = int(cards[i]) # cards는 문자니까 숫자로 변경
        # 장부의 num번 칸에 가서 1 더하기
        count[num] += 1

    # 가장 많이 나온 숫자
    max_num = -1
    # 그때의 카드 장수
    max_count = -1

# max_num : 카드 숫자
# max_count :  장수

    # 장부를 확인
    for i in range(10):
        # 최고값 바꿔주기
        if count[i] >= max_count:
            # 최고 장수로 업데이트
            max_count = count[i]
            # 1등 카드 숫자로 업데이트
            max_num = i


    # 각 줄마다 테스트 케이스 번호 출력, 가장 많은 카드의 숫자와 장 수 차례로 출력
    print(f"#{tc} {max_num} {max_count}")
