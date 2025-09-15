def solution(n):
    answer = []
    i = 1
    while i <= n:
        answer.append(i)
        i += 2
        if i > n:
            break
    return answer

print(solution(10))