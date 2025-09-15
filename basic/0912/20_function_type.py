#반환타입:O 매개변수:O - 자판기
#반환타입:O 매개변수:x - 정수기
#반환타입:x 매개변수:O - 쓰레기통
#반환타입:x 매개변수:x - 마우스

#선언과 사용은 별개의 문제, 이때 들여쓰기를 조심해서 영역을 구분해야한다.
#print는 실질적인 동작이 아니다, 시스템은 이게 뭔지도 모름.

def vendingmc(drink):
    print(f'{drink}를 선택하셨습니다.')
    return(f'{drink}가 나왔습니다.')
print(vendingmc('사이다'))

def waterfountain( ):
    return('물')
print(waterfountain())

def trashcan(trash):
    print(f'{trash}를 버렸습니다.')
trashcan('휴지')

def mouse():
    print('눌렸습니다.')
mouse()


