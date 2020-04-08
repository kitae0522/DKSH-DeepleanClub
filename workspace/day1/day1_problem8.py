'''
FileName : day1_problem8.py
Coder : Song Ki Tae
'''
if __name__ == '__main__':

    height_list = [-1, 150, 190, 170, -1, -1, 160, 180]
    len_height_list = len(height_list)
    for i in range(len_height_list):
        if height_list[i] == -1:
            pass
        else:
            height_list.sort()
            print(height_list)
            break