def fib(n):
    if(n == 0):
        return 0;
    elif(n == 1):
        return 1;
    else:
        return fib(n - 1) + fib(n - 2);

def evenFib():
    sum = 0;
    i = 0;
    while (fib(i) < 4000000):
        fibNum = fib(i);
        if(fibNum % 2 == 0):
            sum += fibNum;
        i+=1;
    return sum;
