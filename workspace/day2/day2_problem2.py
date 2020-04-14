'''
FileName : day2_problem2.py
Coder : Song Ki Tae
'''

import random as ran


def sort_1(num_list):
    for x in range(len(num_list) - 1):
        for y in range(len(num_list) - 1):
            if num_list[y] > num_list[y + 1]:
                num_list[y], num_list[y + 1] = num_list[y + 1], num_list[y]
            elif num_list[y] == num_list[y+1]:
                num_list[y], num_list[y+1] = num_list[y], num_list[y+1]

    return num_list


def sort_2(num_list):
    length = len(num_list) // 2
    half_list1 = num_list[:length]
    half_list2 = num_list[length:]
    for i in range(len(half_list1) - 1):
        for j in range(len(half_list1) - 1):
            if half_list1[j] > half_list1[j + 1]:
                half_list1[j], half_list1[j + 1] = half_list1[j + 1], half_list1[j]

    for o in range(len(half_list2) - 1):
        for p in range(len(half_list2) - 1):
            if half_list2[p] > half_list2[p + 1]:
                half_list2[p], half_list2[p + 1] = half_list2[p + 1], half_list2[p]

    new_num_list = half_list1 + half_list2

    for x in range(len(new_num_list) - 1):
        for y in range(len(new_num_list) - 1):
            if new_num_list[y] > new_num_list[y + 1]:
                new_num_list[y], new_num_list[y + 1] = new_num_list[y + 1], new_num_list[y]

    return new_num_list


def sort_3(num_list):
    for i in range(len(num_list) - 1):
        for j in range(i + 1, len(num_list)):
            if num_list[i] > num_list[j]:
                num_list[i], num_list[j] = num_list[j], num_list[i]

    return num_list


if __name__ == '__main__':

    number = ran.sample(range(1, 50), 6)

    print("정렬 전 리스트={}".format(number))

    sort_1_res = sort_1(number)
    print("sort_1 정렬 결과={}".format(sort_1_res))

    # sort_2_res = sort_2(number)
    # print("sort_2 정렬 결과={}".format(sort_2_res))

    # sort_3_res = sort_3(number)
    # print("sort_3 정렬 결과={}".format(sort_3_res))
