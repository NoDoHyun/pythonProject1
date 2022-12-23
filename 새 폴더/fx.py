def fx(num1):
    if(int(num1)<0):
        print("잘못 입력하셨습니다")
    if(num1.isdigit()==1):
        return int(num1)%7

num1=input()
print(fx(num1))
