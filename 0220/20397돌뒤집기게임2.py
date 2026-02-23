# 전체 테스트 케이스 개수를 입력받음
T = int(input())

for tc in range(1, T + 1):
    # N: 돌의 개수, M: 명령(뒤집기) 횟수
    N, M = map(int, input().split())
    # 현재 돌들의 상태를 리스트로 저장 (0 또는 1)
    arr = list(map(int, input().split()))

    for _ in range(M):
        # i: 기준 돌의 위치(1부터 시작), j: 대칭을 확인할 범위
        i, j = map(int, input().split())
        # 리스트 인덱스는 0부터 시작하므로 기준 위치를 -1 해줌
        mid = i - 1

        # 1부터 j까지 거리를 넓혀가며 대칭 확인
        for step in range(1, j + 1):
            left = mid - step  # 기준 왼쪽 위치
            right = mid + step  # 기준 오른쪽 위치

            # 배열의 범위를 벗어나면 더 이상 확인할 필요 없으므로 중단
            if left < 0 or right >= N:
                break

            # 왼쪽과 오른쪽 돌의 색이 같다면 대칭이므로 둘 다 뒤집음
            if arr[left] == arr[right]:
                # 1에서 현재 값을 빼면 0은 1로, 1은 0으로 반전됨
                arr[left] = 1 - arr[left]
                arr[right] = 1 - arr[right]
            # 만약 대칭이 아니라면 해당 명령의 작업 중단 (문제 조건)
            else:
                break

    # 결과 출력: #테스트케이스번호와 함께 최종 돌 상태를 언패킹(*)하여 출력
    print(f'#{tc}', *arr)