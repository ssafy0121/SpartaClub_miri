# 테스트 케이스
T = int(input())

# T번 만큼 반복한다 (1번부터 T번까지)
for tc in range(1, T + 1):

    # 한 번에 여러 줄이 들어오니까 루프 안에서 input() 해야 함
    # 문자열로 0,1만 주어지는 경우에서는 strip() 쓰기 # 만약 공백이 있으면 계산 틀어짐
    memory = input().strip()

    # 지금 내 상태는 처음에 '0'
    current = '0'

    # 수정 횟수 초기화
    count = 0

    # 문자열 한 글자씩 보면서
    for bit in memory:
        # 목표 비트와 내 현재 상태가 다르면
        if bit != current:
            # 이 위치부터 끝까지 바꿔야 하니까 +1
            count += 1
            # 이제 내 상태도 바뀜
            current = bit

    # 출력
    print(f"#{tc} {count}")