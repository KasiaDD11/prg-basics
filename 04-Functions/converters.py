def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_inch(n):
    return int(n)*0.3937

def feet_ich_to_cm(f,inch):
    inch+=f*12
    return int(inch)*2.54



if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'312 cm = {cm_to_inch(312)}inches')
    print(f'3 feet and 6 inche = {feet_ich_to_cm(3,6)}')

