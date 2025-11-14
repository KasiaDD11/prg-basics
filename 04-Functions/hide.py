def hide(card_number):
    hide=''
    for i in range(len(card_number)):
        if i>1 and i<12:
            hide+='*'
        else:
            hide+=card_number[i]
    return hide
