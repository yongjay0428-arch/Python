import random #랜덤이라는 클래스?를 사용하기 위해서 끌고옴
number = random.randint(1,31) #number이라는 변수에 대해서 1~31 중 하나의 값을 랜덤으로 대입
print(f'내 마음속 숫자:{number}') #랜덤으로 생성된 number 값을 출력
running = True #running이라는 변수에 boolean 값을 참으로 지정
while running: #running이 참인 동안에 14열까지의 과정 반복
    guess = int(input('1~31중 내가 생각한 숫자는?')) #변수 guess에 input()값을 받고, 이를 int 정수값으로 저장
    print(f'입력받은 숫자: {guess}') #받은 guess를 출력
    if guess > number: #입력받은 값이 number에 배정된 값보다 큰 경우
        print(f'{guess}보다 작습니다.') #다운
    elif guess < number: #입력받은 값이 number에 배정된 값보다 작은 경우
        print(f'{guess}보다 큽니다.') #업
    else: #입력받은 값이 number에 배정된 값보다 크지도 작지도 않은 경우 = 같다!
        print('정답!') #정답!!
        running = False  #목표를 달성하였음으로 while 반복문을 멈추기 위해서 running의 boolean 값에 거짓/False를 넣는다.