# 문자 의미
# .	평지(전차가 들어갈 수 있다.)
# *	벽돌로 만들어진 벽
# #	강철로 만들어진 벽
# -	물(전차는 들어갈 수 없다.)
# ^	위쪽을 바라보는 전차(아래는 평지이다.)
# v	아래쪽을 바라보는 전차(아래는 평지이다.)
# <	왼쪽을 바라보는 전차(아래는 평지이다.)
# >	오른쪽을 바라보는 전차(아래는 평지이다.)


# 문자 동작
# U	Up : 전차가 바라보는 방향을 위쪽으로 바꾸고, 한 칸 위의 칸이 평지라면 위 그 칸으로 이동한다.
# D	Down : 전차가 바라보는 방향을 아래쪽으로 바꾸고, 한 칸 아래의 칸이 평지라면 그 칸으로 이동한다.
# L	Left : 전차가 바라보는 방향을 왼쪽으로 바꾸고, 한 칸 왼쪽의 칸이 평지라면 그 칸으로 이동한다.
# R	Right : 전차가 바라보는 방향을 오른쪽으로 바꾸고, 한 칸 오른쪽의 칸이 평지라면 그 칸으로 이동한다.
# S	Shoot : 전차가 현재 바라보고 있는 방향으로 포탄을 발사한다.

T = int(input())
for tc in range(1, T+1):
    # # 문자열 개수
    # H: 높이, W: 너비
    H,W = map(int, input().split())
    # field = [[0]*N for _ in range(N)]

    # 저장 공간
    field = []

    for _ in range(H):
        field.append(list(input()))

    N = int(input())
    # 명령어 문자열
    commands = input()


    # 전차 찾기
    for r in range(H):
        for c in range(W):
            # 전차 발견
            if field[r][c] in ["^", "v", "<", ">"]:
                tank_r = r
                tank_c = c
                direction = field[r][c] # 현재 방향 저장



    # 명령어 문자열
    for cmd in commands:
        if cmd == "U":
            direction = "^"
            field[tank_r][tank_c] = "^"


            # 상하좌우
            # -1, 1, 0, 0
            # 0, 0, -1, 1

            nr = tank_r - 1
            nc = tank_c

            # 범위 안이고 평지면 이동
            if 0 <= nr < H and field[nr][nc] == '.':
                field[tank_r][tank_c] = '.'  # 원래 위치 평지로
                tank_r = nr  # 위치 갱신
                tank_c = nc
                field[tank_r][tank_c] = '^'  # 새 위치에 전차 표시

        elif cmd == "D":
            direction = "v"
            field[tank_r][tank_c] = "v"

            nr = tank_r + 1
            nc = tank_c

            # 범위 안이고 평지면 이동
            if 0 <= nr < H and field[nr][nc] == '.':
                field[tank_r][tank_c] = '.'  # 원래 위치 평지로
                tank_r = nr  # 위치 갱신
                tank_c = nc
                field[tank_r][tank_c] = 'v'  # 새 위치에 전차 표시

        elif cmd == "L":
            direction = "<"
            field[tank_r][tank_c] = "<"

            nr = tank_r
            nc = tank_c - 1

            # 범위 안이고 평지면 이동
            if 0 <= nc < W and field[nr][nc] == '.':
                field[tank_r][tank_c] = '.'  # 원래 위치 평지로
                tank_r = nr  # 위치 갱신
                tank_c = nc
                field[tank_r][tank_c] = '<'  # 새 위치에 전차 표시

        elif cmd == "R":
            direction = ">"
            field[tank_r][tank_c] = ">"

            nr = tank_r
            nc = tank_c + 1

            # 범위 안이고 평지면 이동
            if 0 <= nc < W and field[nr][nc] == '.':
                field[tank_r][tank_c] = '.'  # 원래 위치 평지로
                tank_r = nr  # 위치 갱신
                tank_c = nc
                field[tank_r][tank_c] = '>'  # 새 위치에 전차 표시




        # 포탄 발사
        elif cmd == "S":
            sr = tank_r
            sc = tank_c

            while True:

            # 상하좌우
            # -1, 1, 0, 0
            # 0, 0, -1, 1

                if direction == "^":
                    sr -= 1
                elif direction == "v":
                    sr += 1
                elif direction == "<":
                    sc -= 1
                elif direction == ">":
                    sc += 1

                # 범위 지정
                if not (0<= sr < H and 0<= sc < W):
                    break

                # .	평지(전차가 들어갈 수 있다.)
                # 이거는 앞에서 평지만 들어갈 수 있게 이미 설정함


                # *	벽돌로 만들어진 벽
                if field[sr][sc] == "*":
                    field[sr][sc] = "."
                    break

                # #	강철로 만들어진 벽
                if field[sr][sc] == "#":
                    # 강철 벽은 아무일도 안 일어남
                    # field[sr][sc] = "."
                    break



# 출력
    print(f"#{tc}", end=" ")

    # 맵 한 줄씩 출력
    for row in field:
        print("".join(row))