num1c=0
num1=[]
num2=[]
num3=[]
num4=[]
num5=[]
numdic={1:0,2:0,3:0,4:0,5:0}
spin=0
while(spin<5):
    num1.append(input("행렬1입력"))
    spin+=1
spin=0
for i in range(0,5):
    if num1[i]==num1[i+1] and i > 4:
        num1c += 1
        if num1[i]==num1[i+2] and i > 3:
            num1c += 1
            if num1[i]==num1[i+3] and i > 2:
                num1c += 1
                if num1[i]==num1[i+4]:
                    num1c += 1
print(num1c)

# while(spin<5):
#     num2.append(input("행렬2입력"))
#     spin += 1
# spin = 0
# while(spin<5):
#     num3.append(input("행렬3입력"))
#     spin += 1
# spin = 0
# while(spin<5):
#     num4.append(input("행렬4입력"))
#     spin += 1
# spin = 0
# while(spin<5):
#     num5.append(input("행렬5입력"))
#     spin += 1
# spin = 0




