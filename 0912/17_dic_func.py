dic = {
    'name':'Hong-gill-dong',
    'phone':'010-1234-5044',
    'friends':['Alice','Smith','John']
}

#dic.keys: 특정한 사전의 키들만 가져와 dict_keys라는 객체를 반환한다
print(dic.keys())

for item in dic:
    print(item)

#dick와 리스트 사이 전환
keys= list(dic.keys())
print(keys) #key만 뽑는 이유는 get이나 다른 메서드를 통해서 key=value이기에

#dic.values() : 특정 사전의 값만 가져와 dic_values라는 개체를 반환해
print(dic.values()) #dict_values(['Hong-gill-dong', '010-1234-5044', ['Alice', 'Smith', 'John']])
# list로 변경해서 values에 담아보자
values = list(dic.values())
print(values) #['Hong-gill-dong', '010-1234-5044', ['Alice', 'Smith', 'John']]
print(list(dic.values())) #이렇게 해도 답은 동일하게 나온다.

#dic.items() : 사전의 키: 값들을 한 쌍으로 가져와 dict_items로 반환한다.
print(dic.items())
li = list(dic.items())
print(li)

#값을 가져오기
print(dic.get('name'))
print(dic['phone'])

# dic안에 있는 모든 키와 값을 (키:값)형태로 출력해보자

#키를 뽑아낸 후에 키를 가지고 값을 뽑아내기
for key in dic.keys():
    print(f'{key}:{dic[key]}')

for item in dic.items():
    print(f'{item[0]}={item[1]}')

# print(f'{keys[0]}:{values[0]}')
# print(f'{keys[1]}:{values[1]}')
# print(f'{keys[2]}:{values[2]}')

print('여기부터')

members = {
    'kim':63, 'lee':88, 'park':97, "gang":77, "hwang":100, "ga":65,
    "na":92, "la":90, "wang":100, "gu":79
}

# 90이상인 사람의 이름만 출력 - 해당 key를 찾고 넣어서 밸류 찾기
for key in members.keys():
    if members[key]>=90:
        print(f'"{key}"은(는) 90점을 넘습니다.')
# 90이상인 사람의 이름만 출력 - item을 통해서 찾기
for item in members.items():
    if item[1]>=90:
        print(f'"{item[0]}"은(는) 90점을 넘습니다.')

# key in dic - 있는가? // 특정 키가 있나 없나? 결정하여서 접근할지 안할지
# 검색 시작 여부를 사전에 결정하는 방법
yn = 'kim' in members
print(f'kim이 있는가? {yn}')

yn = 'le' in members
print(f'le가 있는가? {yn}')

print(dic)
#update - 이미 있는 키면 수정을, 없는 키라면 추가를!
dic.update({'name':'홍길동','age':30,'married':False})
print(dic)

#dic.clear() : 사전안의 내용을 모두 지운다
dic.clear()
print(dic)