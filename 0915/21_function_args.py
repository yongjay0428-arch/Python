from ctypes import HRESULT


def plus(num) :
    result = num+5
    return result

print (plus(5))
#print (plus()) # plus() missing 1 required positional argument: 'num'

#튜플은 수정이 불가능한 인자 형태이다. 튜플의 특징으로는 소괄호 사용과 수정이 불가하다!
def tuple_args(*numbers):
    print(numbers) #변수 앞의 *은 포인터, 변수마다 메모리를 직접 지정가능 -C / 우리는 인자종류 지정
    total = 0
    for num in numbers:
        total += num
    return total
#해당 방식은 사용자가 인자값의 개수를 자유롭게 정해서 넣을 수 있다!
print(tuple_args(1,2,3,4,5))

# 별 두개짜리는 뭐냐? - 매개변수를 사전형태로 받겠디.
def dic_args(**dic):
    #내가 하고싶은건? dic에서 값을 빼온다 -> 값들을 하나씩 더해서 누적시키고 -> 누적된 값을 밖으로 뱉는다
    result =0
    for i in dic.values():
        result +=i
    print(result)

    # result=0
    # for key in dic.keys():
    #     result += dic[key]
    # print(result)
    #
    # result=0
    # for items in dic.items():
    #     result += items[1]
    # print(result)
    #
    # print(sum(dic.values()))

dic_args(kim=50,lee=100,pakr=70,na=90)
