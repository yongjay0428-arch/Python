import traceback

num_list = [1,2,3,1,2,3,1,2,3,1,2,3,4,5,6]

idx = 0

try:
    while True:
        idx = num_list.index(3, idx)
        print(f'3은 {idx}인덱스에 있습니다') #ValueError: 3 is not in list
        idx +=1
except ValueError as e:
    print(e) #예외에 대한 대략적인 정보 출력
    traceback.print_exc() #상세한 예외 정보를 보여준다.
    print ('더 이상 3을 찾을 수 없습니다')
finally:
    print('====끝====')