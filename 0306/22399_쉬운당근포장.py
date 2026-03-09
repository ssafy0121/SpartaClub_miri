#N개의 당근을 주문하면 대, 중, 소 상자로 구분해 포장해야 한다.
#같은 크기의 당근은 같은 상자에 들어있어야 한다.
# 뽑아온 당근이 3개이고, 크기가 1 2 3이라면 다음과 같이 포장할 수 있다.
# 소 [ 1 ], 중 [ 2 ], 대 [ 3 ], 상자에 든 당근의 개수 차이는 0

# 당근이 5개이고 크기가 1 1 1 2 3 이라면, 조건 (1)~(3)을 만족하는 포장은 다음과 같다.
# 소[ 1 1 1 ], 중 [ 2 ], 대 [ 3 ], 당근의 개수 차이는 2

T = int(input())
for tc in range(1, T+1):

    N = int(input())

    carrots = list(map(int, input().split()))

    # 입력값이 정렬되도록
    carrots.sort()

    result = 10000

    # 첫 상자 하고 뒤에 적어도 두 상자 필요하니 인덱스 N-1
    for i in range(1, N-1):

        # 당근을 1,1,1 / 1,2 이렇게 하면 안 됨
        if carrots[i-1] == carrots[i]:
            continue

        # 첫 상자 그 다음이니 i+1이고 N
        for j in range(i+1, N):

            if carrots[j - 1] == carrots[j]:
                continue

            box1 = carrots[:i]
            box2 = carrots[i:j]
            box3 = carrots[j:]

            cnt1 = len(box1)
            cnt2 = len(box2)
            cnt3 = len(box3)


            max_cnt = max(cnt1, cnt2, cnt3)
            min_cnt = min(cnt1, cnt2, cnt3)

            diff = max_cnt - min_cnt

            if diff < result:
                result = diff

    if result == 10000:
        result = -1

    print(f"#{tc} {result}")



