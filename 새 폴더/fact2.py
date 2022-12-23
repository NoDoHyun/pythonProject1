def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

num=int(input())
for i in range (0,num+1):
    if(fib(i)<num):
        print(fib(i))