# sys.setrecursionlimit(limit) to alleviate recursive limits

def largestPrimeFactor(num):
    for i in range(num, 0, -1):
        if(num != i and i != 1):
            if(num % i == 0):
                return largestPrimeFactor(i);
    return num;

# a = number
# b = increment
# c = divisor

# largestPrimeFactor
# (a = numberToCheck)
# (b = 2)
# (c = 0)
def betterLargestPrimeFactor(a, b, c):
    if(a == b):
        return a;
    if(a % b == 0):
        a = a / b;
        c = b;
        b = 2;
        return betterLargestPrimeFactor(a, b, c);
    else:
        return betterLargestPrimeFactor(a, b + 1, c);

# best method (source: stackoverflow)
def lpf(a):
    b = 2;
    while (a > b):
        if (a % b ==0):
            a = a / b;
            b = 2;
        else:
            b += 1;
    print("Largest Prime Factor: %d" % (b));
