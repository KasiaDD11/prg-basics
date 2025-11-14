###
# Functions to read any data type from the keyboard
#
def input_string(message):
    wiad = input(message)
    return wiad

def input_integer(message):
    wiad = int(input(message))
    return wiad

def input_real(message):
    waid= float(input(message))
    return waid

def input_boolean(message):
    wiad = (input(message))
    if wiad=='y':
        return True
    else:
        return False