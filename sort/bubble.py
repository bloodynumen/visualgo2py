# -*- coding: utf-8 -*-

random_list = [3, 1, 66, 2, 4, 6, 32, 19, 0, 1, 33]

def bubble(random_list = []):
    times = len(random_list) - 1
    if times <= 0:
        return random_list
    end = times
    for i in range(0, times):
        for j in range(0, end):
            if random_list[j] > random_list[j + 1]:
                random_list[j],random_list[j + 1] = random_list[j + 1], random_list[j]
        end = end - 1
    return random_list

print(bubble(random_list))
