def f(n):
    jed=0
    dwa=1
    if n==1:
        return jed
    elif n==2:
        return dwa
    else:
        for i in range (n-2):
            pomoc=dwa
            dwa=dwa+jed
            jed=pomoc

    return dwa

print(f(9))