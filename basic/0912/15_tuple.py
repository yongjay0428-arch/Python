tu1 = (1,2,3,)#tuple은 대괄호가 아닌 소괄호로 선언된다.
tu2 = ("a","b","c")
tu3 = (1,2,('a','b'))

#불러오기
print(tu1[1])
#slicing
print(tu2[1:])
#더하기
print(tu1+tu2)
print(tu1*3)
#만약 list와 tuple 사이를 전환해야한다면?
tu2list = list(tu2)
print(f'{tu2} --> {tu2list}') #('a', 'b', 'c') --> ['a', 'b', 'c']
#이제부터는 값을 편집할 수 있게된다.
list2tu = tuple(tu2list)
print(f'{tu2list} --> {list2tu}') #['a', 'b', 'c'] --> ('a', 'b', 'c')