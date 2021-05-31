from random import uniform
def monte_carlo(n):
    i=1
    num = 0.0
    den = 0.0
    for i in range (n):
        x = uniform(-1,1)
        y = uniform(-1,1)
        if(x*x + y*y < 1):
            num = num+1
        den = den+1
    return 4*num/den