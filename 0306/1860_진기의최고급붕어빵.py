### : AI한테 도움받은 부분 표시
# AI 안 쓰고 풀도록 시간 텀 두고 반복해서 풀어보는 시간을 갖겠습니다.


T = int(input())
for tc in range(1, T+1):

# N명의 사람이 자격
# 진기는 0초부터 붕어빵을 만들기 시작하며,
# M초의 시간을 들이면 K개의 붕어빵을 만들 수 있다.
# 2 2 2
# 손님 2명, 2초마다 붕어빵 2개 생산
    N,M,K = map(int,input().split())

# 각 정수는 각 사람이 언제 도착하는지를 초 단위로 나타낸다.
# 3 4
# 손님들 3, 4초마다 옴
    customer = list(map(int,input().split()))

    # 가장 먼저 오는 손님부터 차례대로 빵을 줄 수 있는 지 확인해야 함
    ### 오름차순 안 하니 출력값 틀립니다.
    customer.sort()

    result = "Possible"

    # 손님 확인
    for i in range(N):
        customer_arrive = customer[i]

        # M초의 시간 K개 생산
        # 손님 도착까지 만들어진 붕어빵 개수
        made_bread = (customer_arrive // M) * K

        ### 이 부분 AI한테 도움 받았습니다.
        # 처음에 need_bread = i 적었다가 인덱스 오류났습니다.
        need_bread = i + 1

        if made_bread < need_bread:
            result = "Impossible"
            break

    print(f"#{tc} {result}")