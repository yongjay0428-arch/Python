#사전은 key:값의 형태로 되어있다
#비슷한 자료구조로는 자바스크립트의 오브젝트, 자바의 맵 등이 있다.
dic={'name':'kim_ji_hoon',
     'phone':'010-1234-5044',
     'age': 55
 }
dic2 ={
    'name':'hong,gil-dong',
    'phone':'010-2233-5454',
    'friends':['alice','john','smith']
}
#사전에 데이터 넣기1
a = {'first':'a' }
print(a)
#사전에 데이터 넣기2
a['second'] = 'b'
print(a)
a['name'] = 'john'

print(a)
#사전에서 특정 요소 삭제
del a['second']
print(a)

#사전에서 특정 요소를 꺼내보자!
print(dic2['name'])
print(dic2['friends'])
#get 메서드를 활용해서도 가져올 수 있다.
print(dic.get('phone'))
print(dic2.get('nick','해당 내용이없음')) #None이지만 뒤에 넣으면 저걸로 나온다