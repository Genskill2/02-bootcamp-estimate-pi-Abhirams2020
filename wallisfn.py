def wallis(n):
    #hello
   
    p = 1.0
    for i in range(1,n):
        p = p*4*i*i/(4*i*i-1)
    return 2*p
