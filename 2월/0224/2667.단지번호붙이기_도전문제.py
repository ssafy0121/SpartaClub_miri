N = int(input())
apart = [list(map(int, input().strip())) for _ in range(N)]

# 델타 (상, 하, 좌, 우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# BFS 함수
def bfs(start_r, start_c):
    # 빈 리스트에 시작 위치
    queue = [(start_r, start_c)]

    # 시작 지점 방문 처리 (재방문 방지)
    apart[start_r][start_c] = 0
    count = 1  # 현재 집 개수 1개

    # 대기열에 확인할 집이 남아있는 동안 반복
    while queue:
        # 리스트의 맨 앞(0번 인덱스)에서 좌표를 꺼냅니다.
        # pop(0)은 deque의 popleft()와 똑같은 역할을 합니다.
        r, c = queue.pop(0)

        # 4방향 델타 탐색
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 지도 범위 안이고, 아직 방문 안 한 집(1)을 발견하면?
            if 0 <= nr < N and 0 <= nc < N and apart[nr][nc] == 1:
                # 방문 표시하고 개수 올리기
                apart[nr][nc] = 0
                count += 1
                # 다음 탐색을 위해 대기열(queue) 끝에 추가
                queue.append((nr, nc))

    return count


# 4. 전체 지도 뒤지기
ans = []
for r in range(N):
    for c in range(N):
        if apart[r][c] == 1:
            # 집을 찾을 때마다 bfs 엔진 가동!
            ans.append(bfs(r, c))

# 5. 결과 출력
print(len(ans))  # 총 단지 수
ans.sort()  # 오름차순 정렬
for c in ans:
    print(c)