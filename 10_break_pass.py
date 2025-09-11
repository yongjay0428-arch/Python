cup = 0
while True:
    cup +=1
    print (cup)
    if cup == 10:
        break # or running = True & running = False 사용하기
print ('while문 종료!')


for i in range (1,10):
    if i%3==0:
        continue
    print(i)