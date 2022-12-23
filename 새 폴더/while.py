coffee = 10
money=0
while(1):
    select=int(input("입력\n"))
    if select==1:
        money=int(input("돈투입"))
    if select==2:
        if coffee>0 and money>=100:
            print("커피있음\n")
            coffee-=1
            money-=100
        if money<100:
            print("돈부족")
        if coffee==0:
            print("커피없음")
            break
