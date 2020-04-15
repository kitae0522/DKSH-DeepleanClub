'''
FileName : day2_problem1.py
Coder : Song Ki Tae
'''


if __name__ == '__main__':

    # a = [1, 5, 7, 6, 5, 8, 3]
    # su = 0
    #
    # for i in range(len(a)):
    #     if i % 2 == 1:
    #         su += a[i]
    # print(su)

    line_max = 8
    for line in range(line_max + 1):
        if line < 1:
            print("       *", end=" ")
        else:
            for space in range(line):
                print(" ", end="")
            for star in range(line_max - line):
                print("*", end="")
        print()