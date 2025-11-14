def f(amount_to_pay):
    coins=0
    c=[]
    while amount_to_pay>0:
        if amount_to_pay>=5:
            coins+=1
            c.append(5)
            amount_to_pay-=5
        elif amount_to_pay>=2:
            coins+=1
            c.append(2)
            amount_to_pay-=2
        elif amount_to_pay>=1:
            coins+=1
            c.append(1)
            amount_to_pay-=1
    print(c)
    return coins


print(f(23)) 
print(f(8))
print(f(2) )
print(f(0))