#문자열은 '' "" 모두 사용 가능하다.
name='lee yong-jay'
content = "my content"

#여러줄의 믄자열을 변수에 담을때
multi = '''this is multi line string
this is second line'''

print ('name:'+name)
print ('content:' +content)
print ('multi:' +multi)

# 문자열에 다른 타입의 데이터를 함께 출력할 경우...
#f-string 이전의 버젼, 구버젼에서 신버젼으로 바꾸는 경우에 사용된다.
age = 22
print('내 이름은 {0}이고 나이는 {1}입니다.'.format(name,age))
#자바에서는 매개변수의 타입이 지정되기에 가독성 문제 없음, 그러나 파이선에서는 따로 신호를 준다.
print('내 이름은 '+name+'이고, 나이는 '+str(age)+'입니다')
print (f'내 이름은 {name}이고, 나이는 {age}입니다.')
#출력은 컴퓨터가 아닌 우리가 확인하기 위한 수단

#다중라인처리, 여러 줄일 경우에 한줄로 처리하거나 한줄을 여러줄처럼 줄바꿈하기
print('이것은 한 줄 이지만 \n 여러줄처럼 보이게 할겁니다.') #new line
print('이것은 두 줄 이지만 \
한줄 처럼 보이게 할겁니다.')
#자바는 ;으로 줄바꿈을 인식하지만 파이썬은 줄바꿈으로 인식하게 추가 작업 요구됨



