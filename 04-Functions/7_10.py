def f(x,y):
    neg=0
    for i in range(x,y+1):
        if i<0 and i%2==0:
            neg+=1

    return neg

print(f(-7,8)) #returns 3
print(f(-1,11))# returns 0