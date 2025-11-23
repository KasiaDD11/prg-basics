def occurs(number,arr):
    if number in arr:
        return 'appears'
    else:
        return 'does not appear'
        
        

number=2
arr=[15,38,7,23,14]
print(f'Number: {number}')
print(f'Array: {" ".join(map(str,arr))}')
print(f'Result: number {number} {occurs(number,arr)} in the array')