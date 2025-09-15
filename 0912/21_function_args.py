def plus(num) :
    result = num+5
    return result

print (plus(5))
#print (plus()) # plus() missing 1 required positional argument: 'num'

#튜플은 수정이 불가능한 인자 형태이다. 튜플의 특징으로는 소괄호 사용과 수정이 불가하다!
def tuple_args(*numbers):
    print(numbers) #변수 앞의 *은 포인터, 변수마다 메모리를 직접 지정가능 -C / 우리는 인자종류
    total = 0
    for num in numbers:
        total += num
    return total
print(tuple_args(1,2,3,4,5))