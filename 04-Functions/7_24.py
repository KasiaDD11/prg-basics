def f(expression):
    result = int(expression[0])   # pierwsza cyfra
    i = 1

    while i < len(expression):
        op = expression[i]        # operator + lub -
        num = int(expression[i+1])# następna cyfra

        if op == "+":
            result += num
        else:
            result -= num

        i += 2  # przechodzimy do następnego operatora

    return result


print(f("2+3"))
print(f("3+8+1"))
print(f("2+3-4+5-0"))