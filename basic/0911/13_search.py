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

#b라는 리스트 내부 모든 3의 위치를 보여주는 프로그램
b = [3,4,1,2,3,4,5,6,1,3,2]

# idx = 0 #변수 idx 생성 및 0 지정, 스트링의 맨 앞 인덱스에서 시작하도록
# while True: # while 반복문 시작, 멈추지 않고 돌아가도록 True
#     idx = b.index(3,idx) #시작은 idx=0, 0 이상의 3이 존재하는 인덱스를 찾고,
#     # 해당 인덱스 값 다음 인덱스부터 또 찾도록하기 위해서 마지막에 idx +=1
#     print (f'3의 값은 {idx}번에 있다.') # f-string을 통해서 3의 위치 출력
#     idx +=1 #이후 index(3,idx)가 더이상 찾을 3이 없기 때문에 구동이 멈추기에 별도의 break는 넣지 않는다.

# idx=0
# for n in b: # for in을 사용하면 리스트에 있는 값을 하나씩 뽑아낸다
#     if n == 3:
#         print(f'3이 있는 인덱스:{idx}')
#         idx +=1

# #리스트 요소 삭제
# #del a[3]와 a.remove(3)
# #del은 특정 인덱스(위치)의 값을 지운다
# #remove는 해당 값을 지운다.(한개만)

# print(f'a:{a}')
#  a.remove(3)
#  print(f'a:{a}')

# #pop()  = append()의 반대격 개념 / 뒤에서부터 날아간다
# #맨 마지막 요소를 빼내고(리스트에서 사라진다)
# val = a.pop()
# print(f'빼낸 값: {val} /a:{a}')
# val = a.pop()
# print(f'빼낸 값: {val} /a:{a}')
#
# #리스트확장(더하기와 비슷한 개념)
# print(a)
# a.extend(b) # a+b와 동일한 개념
# print(a)
#
# # 특정한 값이 해당 리스트에 몇개 있는지 확인함
# print(a)
# print(f'a안에 9은 {a.count(9)}개 가 있다.') #없는 값에 대해서는 0을 반환

#a안에 있는 모든 3을 지워주세요
# for n in a:
#     if n == 3:
#         a.remove(3)
# print(a)

while True:
    a.remove(3)
    if a.count(3) == 0:
        break
    print(a)