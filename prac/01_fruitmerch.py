def solution(k, m, score):
    score.sort(reverse=True)
    answer = 0
    n=0
    box=len(score) // m
    for i in range(box):
            answer += score[m-1]*m
            for m1 in range(m):
                score.pop(0)
                if len(score) < m:
                    break
    return answer

    answer=0
    box=len(score)//m
    for i in range(1,box+1):
        answer+= min(score[(i-1)*m:m*i-1])*m
    return answer
print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))

