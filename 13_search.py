# 특정한 자료 덩어리에서 원하는 값을 찾는 것을 의미한다.
a = [ 3,4,1,2,3,4,'G','F','G']
# 원하는 값의 인덱스 찾기
#2라는 값이 어느 위치에 있는가?
print (f'2는 어디?:{a.index(2)}')
print (f'G는 어디?:{a.index('G')}') #해당 경우에 G가 두개지만 하나만 보여준다.
#5번 인덱스부터 'G'를 찾아라 -> 확실한 경우 검색속도향상하기 위해서
print (f'G는 어디?:{a.index('G',5 )}')
#값이 없다면 에러(예외)를 발생시킨다.

# print(a.index('H')) ValueError: 'H' is not in list

b = [3,4,1,2,3,4,5,6,1,3,2]

idx = 0
while True:
    idx = b.index(3,idx)
    print (f'3의 값은 {idx}번에 있다.')
    idx +=1
    # if idx == len(b):
    #     break

for n in b: # for in을 사용하면 리스트에 있는 값을 하나씩 뽑아낸다
    if n == 3:
        print(f'3이 있는 인덱스:{idx}')
        idx +=1

