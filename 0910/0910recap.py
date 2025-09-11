import random
number = random.randint(1,100)
print(f'문제 출제 완료!')
running = True
count = 0
while running:
    ans = int(input(f'1에서 100 사이의 정답을 입력하십시오, {7-count}번 더 시도하실수 있습니다'))
    count += 1
    if ans < 1 or ans >100:
      print("범위 밖의 숫자입니다")
    else:
        if ans > number:
            print('다운')
        elif ans < number:
            print('업')
        else:
            print(f'정답입니다!! number = {number}')
            running = False
    if count >= 7 and ans != number:
        print(f'시도 횟수를 초과하였습니다, 정답은 {number}였습니다')
        running = False