def fibo(num):
    for i in range(0,num):
        if num<=1:
            print(i)
            return int(fibo(num))+i
        # if num>=2:
        #     print(i)
        #     num1=i+(i-1)
        #     print(num1)
        #     return int(fibo(num))+i

num=int(input())
fibo(num)