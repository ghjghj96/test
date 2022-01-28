import random
b = random.randint(1,10)
cnt=0
list=[]
while cnt <5:
    a = int(input("숫자를 입력하시오"))
    if a == b:
        list.append(a)
        print("정답입니다.")
        break
    elif a>b :
        cnt+=1
        list.append(a)
        print(" 랜덤숫자보다 큽니다.", (5-cnt),"회 남았습니다.")
    elif a<b :
        cnt+=1
        list.append(a)
        print("랜덤숫자보다 작습니다.", (5-cnt),"회 남았습니다.")
print("입력하신 숫자들는 {} 입니다".format(list))
