'''
FileName : day2_problem1.py
Coder : Song Ki Tae
'''


if __name__ == '__main__':

    print(" " * 6 + "*" + " " + "*")
    for j in range(7, 0, -1):
        left = " " * (7 - j) + "*" * j
        right = "*" * j
        print(left + " " + right)