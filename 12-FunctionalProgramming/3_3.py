stock = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]
lista=map(lambda x:x[0]*x[1],stock)
lista=list(lista)
print(sum(lista))