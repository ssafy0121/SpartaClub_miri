# 병합 정렬 함수
# arr를 받아서 정렬된 새로운 리스트를 반환

def merge_sort(arr):
    # count를 전역변수로 사용할 것이므로 global 선언
    # global 쓰는 대표 상황: 병합정렬/DFS/백트래킹
    global count

    # 종료 조건
    # 원소가 1개이면 이미 정렬된 상태이므로 그대로 반환
    if len(arr) <= 1:
        return arr

    # 가운데 위치 계산
    mid = len(arr) // 2

    # 왼쪽 절반을 병합 정렬
    left = merge_sort(arr[:mid])

    # 오른쪽 절반을 병합 정렬
    right = merge_sort(arr[mid:])


    # 문제에서 요구한 추가 조건 검사
    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 크면 count 증가
    if left[-1] > right[-1]:
        count += 1

    # 이제 left와 right를 하나로 합치기 위한 리스트
    merged = []

    # 왼쪽 리스트를 가리키는 인덱스
    l = 0

    # 오른쪽 리스트를 가리키는 인덱스
    r = 0

    # 두 리스트를 비교하면서 작은 값을 merged에 넣는다.
    while l < len(left) and r < len(right):

        # 왼쪽 값이 더 작거나 같으면 왼쪽 값을 넣는다.
        if left[l] <= right[r]:
            merged.append(left[l])
            l += 1

        # 오른쪽 값이 더 작으면 오른쪽 값을 넣는다.
        else:
            merged.append(right[r])
            r += 1

    # 왼쪽 리스트에 남은 값이 있으면 뒤에 붙인다.
    while l < len(left):
        merged.append(left[l])
        l += 1

    # 오른쪽 리스트에 남은 값이 있으면 뒤에 붙인다.
    while r < len(right):
        merged.append(right[r])
        r += 1

    # 병합이 끝난 정렬된 리스트 반환
    return merged


# 테스트케이스 개수 입력
T = int(input())

# 1번 테스트케이스부터 T번 테스트케이스까지 반복
for tc in range(1, T + 1):
    # 정수의 개수 입력
    N = int(input())

    # 정수 리스트 입력
    arr = list(map(int, input().split()))

    # 문제에서 세어야 하는 횟수 초기화
    count = 0

    # 병합 정렬 수행
    result = merge_sort(arr)

    # 정렬된 리스트의 가운데 원소와 count 출력
    print(f"#{tc} {result[N // 2]} {count}")