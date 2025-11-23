arr=['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
arr2=sorted(arr,key=len)
print(f'names: {" ".join(map(str,arr))}')
print(f'longest name: {arr2[-1]}')