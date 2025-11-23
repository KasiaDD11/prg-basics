import random as R
arr=['ad','da','dee',4,8,1]


def rand_elem(array):
    for i in range(4):
        print(R.choice(array))

rand_elem(arr)