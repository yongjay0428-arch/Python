# set은 순서가 없고 중복을 허용하지 않는다!  로또볼과 같은 형태
number_set = set([1,2,3])
print(number_set)

#중복이면 안받아 버리니까 그냥 그 용도로 사용해도 된다
str_set = set("Helloworld")
print(str_set)

listset=list(str_set)
print(listset)
#set들을 이용해서 집합을 구현할 수 있다! /
s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9]) #두 세트에는 중복되는 값이 없다.

#교집합 - intersection
#합집합 - union
#차집합 - minus|difference
print(f'합집합1:{s1 | s2}') #합집합
print(f'합집합2:{s1.union(s2)}')
print(f'교집합1:{s1 & s2}') #-교집합!
print(f'교집합2:{s1.intersection(s2)}')
print(f'차집합1:{s1 - s2}'); print(f'차집합1:{s2-s1}') #차집합 시에 앞뒤 주의!
print(f'차집합2:{s1.difference(s2)}') #차집합!

#값 한개 추가하기
s1.add(10)
print(s1)
#값 여러개 추가하기
s1.update([10,20,30])
print(s1)
#특정 값 제거하기ㅇ
s1.remove(10)
print(s1)
# s1.remove(10)
# print(s1) - KeyError: 10 !없는 값을 지우려고 했기 때문에 keyerror발생

s1.discard(10) #remove와 동일하지만 없는거 지워도 에러가 나지 않는다
