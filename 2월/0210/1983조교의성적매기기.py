#입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    # 학점
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    scores = []
    for _ in range(N):
        mid, final, assign = map(int, input().split())
        # 총점 비율
        total = (mid*0.35) + (final*0.45) + (assign*0.20)
        scores.append(total)

    # K번째 학생의 점수
    K_score = scores[K-1]

    # K번째 학생이 몇 번째 등수인지 확인
    K_rank = 0
    for s in scores:
        # K보다 점수가 높다면 K의 등수는 밀려남
        if s > K_score:
            K_rank += 1
    # 학점 배분: N/10명씩
    people = N // 10

    # 문제에서 원하는 답
    result = grade[K_rank//people]

    #테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
    print(f"#{tc} {result}")