def fibonacciModified(t1, t2, n):
    fib_num=[t1,t2]
    n-=2
    while n!=0:
        new_num=fib_num[len(fib_num)-2]+(fib_num[len(fib_num)-1]**2)
        fib_num.append(new_num)
        n-=1
    return fib_num[len(fib_num)-1]