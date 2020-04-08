'''
FileName : day1_problem7.py
Coder : Song Ki Tae
'''
if __name__ == '__main__':

    inputArray = ["aba", "aa", "ad", "vcd", "aba"]      # inputArray 배열 값들 선언
    length = len(inputArray)        # inputArray 배열 길이 파악
    for i in range(length):        # inputArray 배열 길이만큼 반복
        maxLen = max(length[i])     # 여기서 왜 오류가 뜨는지 잘 모르겠음
    print(maxLen)
