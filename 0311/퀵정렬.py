# 퀵 정렬을 구현해 N개의 정수를 정렬해 리스트 A에 넣고
# A[N//2]에 저장된 값을 출력하는 프로그램을 만드시오.


def quick_sort(left, right):

    # 종료 조건
    # 정렬할 구간이 1 이하이면 정렬 끝
    if left >= right:
        return

    # 기준값을 가장 왼쪽 값으로 선택
    pivot = A[left]

    # 왼쪽과 오른쪽에서 이동할 포인터
    i = left + 1
    j = right

    # i와 j가 서로 교차할 때까지 반복
    while i <= j:

        # 기준값보다 작은 값이면 계속 오른쪽을 이동
        while i <= j and A[i] <= pivot:
            i += 1

        # 기준보다 큰 값이면 계속 왼쪽으로 이동
        while i <= j and A[j] >= pivot:
            j -= 1

        # 서로 위치가 바뀌어야 할 경우
        if i < j:
            A[i], A[j] = A[j], A[i]

    # 기준 위치 교환
    A[left], A[j] = A[j], A[left]

    # 기준으로 왼쪽 부분 정렬
    quick_sort(left, j-1)

    # 기준으로 오른쪽 부분 정렬
    quick_sort(j+1, right)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))


    # 퀵 정렬 실행
    quick_sort(0, N-1)

    # 가운데 값 출력
    print(f"#{tc} {A[N//2]}")



