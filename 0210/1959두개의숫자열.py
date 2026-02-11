# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
T = int(input())
for tc in range(1, T+1):

    # 각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 더 긴 쪽의 양끝을 못 벗어나게 지정
    if N > M:
        A, B = B, A
        N, M = M, N

    #서로 마주보는 숫자들을 곱하고 모두 더할 때 최대값
    # inf 는 무한대
    max_total = -float('inf')

    # 움직일 수 있도록
    # 큰 값M - 작은 값 N
    for i in range(M-N+1):
        sum = 0

        # 마주보는 칸끼리 곱하기
        # A의 J번째 칸과 옆으로 i만큼 밀린 B의 (i+j)와 만남
        for j in range(N):
            sum += A[j] * B[i+j]

        # 최대값
        # 변수 위치 주의: (바뀔 변수) = (새로운 값)
        if sum > max_total:
            max_total = sum

    # 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
    print(f"#{tc} {max_total}")