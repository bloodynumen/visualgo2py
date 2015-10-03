# -*- coding: utf-8 -*-

random_list = [3, 1, 66, 2, 4, 6, 32, 19, 0, 1, 33]

def quick(left, right):
    if left >= right:
        return
    datnum = random_list[left]
    i = left
    j = right
    while(i != j):
        while(i < j and random_list[j] >= datnum):
            j = j - 1
        while(i < j and random_list[i] <= datnum):
            i = i + 1
        if i != j:
            random_list[i],random_list[j] = random_list[j], random_list[i]
        print(random_list)
    #swap
    random_list[left],random_list[i] = random_list[i],random_list[left]
    quick(left, i - 1)
    quick(i + 1, right)

print(random_list)
quick(0, len(random_list) - 1)
print(random_list)

