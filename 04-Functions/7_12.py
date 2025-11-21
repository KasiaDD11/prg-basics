def znaki(n):
    if n==1:
        return "*"
    else:
        znak=""
        for i in range(n-1):
            znak+="*/"
        znak+="*"
        return znak
    

print(znaki(1))
print(znaki(2))