import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct
otwarte='[{('
zamykane=']})'

def brackets_ok(expression):
    nawiasy = queue.LifoQueue()
    for znak in expression:
        if znak in otwarte:
            nawiasy.put(znak)
        elif znak in zamykane:
            if zamykane.index(znak)!=otwarte.index(nawiasy.get()):
                print('caput')
                return False
    if nawiasy.empty():
       return True
    else:
       print('zle')
       return False
               
   
   
   
    #True if brackets in expression are ok of False otherwise

if brackets_ok(expression1):
   print('GOOD')
else:
   print('BAD')

if brackets_ok(expression2):
    print('GOOD')
else:
    print('BAD')

if brackets_ok(expression3):
    print('GOOD')
else:
    print('BAD')