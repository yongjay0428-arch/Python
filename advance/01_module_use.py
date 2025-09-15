#from 모듈 import 함수
#하나는 사용할 함수를 부르는 것
from oper import sum
print(f'sum함수 실행:{sum(5, 10)}')

#import 모듈
#일단 모듈 불러놓고 모듈에서 원하는 함수를 사용하는 방법
import oper as op
print(f'minus 함수 실행: {op.minus(10, 5)}')

# 변수도 불러올 수 있다
print(f'field1:{op.field1} / field2:{op.field2}')