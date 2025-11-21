def f(a,b,znak):
    if znak=="+":
        return a+b
    
    if znak=="-":
        return a-b
    
    if znak=="%":
        return a%b
    
    if znak=="*":
        return a*b
    
    if znak=="**":
        return a**b
    
print(f(2,3, "+"))
print(f(2,3, "%") )
print(f(2,3, "**") )
print(f(2,3, "*") )
print(f(2,3, "-") )
    
