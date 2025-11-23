

def f(dice):
    current = dice[0]      
    longest_digit = dice[0] 
    current_len = 1
    longest_len = 1

    for i in range(1, len(dice)):
        if dice[i] == current:
            current_len += 1
        else:
            current = dice[i]
            current_len = 1

        if current_len > longest_len:
            longest_len = current_len
            longest_digit = current

    return longest_digit


print(f("5233165554211"))
print(f("2133"))