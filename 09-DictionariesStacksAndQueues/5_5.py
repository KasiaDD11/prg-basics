paragraph = "cat dog mouse cat rat cat mouse"
slowa=paragraph.split()
slownik={}
for slowo in slowa:
    if slowo not in slownik:
        slownik[slowo]=1
    else:
        slownik[slowo]+=1

print(slownik)