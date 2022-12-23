num=int(input("단 입력\n"))
num2=int(input("곱할 수\n"))
for i in range(1,num2+1):
    print("%dx%d=%d"%(num,i,num*i), end=" ")
print("\n")