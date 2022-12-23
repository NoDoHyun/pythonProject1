str1=input("알파벳 입력")
num1=int(input("숫자 입력"))
num2=ord(str1)*num1
if(num2<10):
    print("0000000%d"%num2)
if(10<=num2<100):
    print("000000%d"%num2)
if(100<=num2<1000):
    print("00000%d"%num2)
if(1000<=num2<10000):
    print("0000%d"%num2)
if(10000<=num2<100000):
    print("000%d"%num2)
if(100000<=num2<1000000):
    print("00%d"%num2)
if(1000000<=num2<10000000):
    print("0%d"%num2)
if(10000000<=num2<100000000):
    print("%d"%num2)