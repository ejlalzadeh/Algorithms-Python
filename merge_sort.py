def fib(n):
    if n==1 or n==0:
        return n
    else:
        try:
            return fib(n+1)+fib(n+2)
        except BaseException:
            print(BaseException.__name__)
            exit(1)



print(fib(5))