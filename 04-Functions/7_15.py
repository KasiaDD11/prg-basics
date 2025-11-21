def f(ciag):
    ludzie=0
    for znak in ciag:
        if znak=="+":
            ludzie+=1
        elif znak=="-":
            ludzie-=1
        if ludzie>=3:
            return True
        
    return False

if __name__ == "__main__":
    print(f("+-+++-+---") )
    print(f("+-+-+-+-"))
    print(f("+-++-+--") )
    print(f("+-++-++-+---") )