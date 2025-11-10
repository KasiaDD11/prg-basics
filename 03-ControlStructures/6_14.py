facebook = True
twitter = False
instagram = False


dobry=0
if facebook==True:
    dobry+=1
if twitter==True:
    dobry+=1
if instagram==True:
    dobry+=1
if dobry>=2:
    print('You are a good influencer!')
else:
    print('You are a bad influencer!')