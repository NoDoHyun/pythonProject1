strnum=input("입력\n") # 1, 5, 7, 4, 2, 10, 11, 20, 11 같은 형태로 입력해야함
strnum2=strnum.split(",")
count=0
for i in strnum2:
    if int(i)%2==0:
        count+=1
print("짝수의수:",count)
