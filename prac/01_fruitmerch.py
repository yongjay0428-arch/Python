def solution(k, m, score):
    score.sort(reverse=True)
    answer=0
    box=len(score)//m
    for i in range(1,box+1):
        answer+= min(score[(i-1)*m:m*i])*m
        if len(score) < m:
            break
    return answer
#https://school.programmers.co.kr/learn/courses/30/lessons/135808