'''
FileName : day1_problem6.py
Coder : Song Ki Tae
'''

if __name__ == '__main__':

    inputArray = [3, 6, -2, -5, 7, 3]      # inputArray 배열 값들 선언
    length = len(inputArray)   # inputArray 배열 길이 파악
    number = []     # [3*6, 6*(-2), (-2)*(-5), (-5)*7, 7*3] 값들이 들어갈 배열들

    for i in range(length - 1):
        number.append(inputArray[i] * inputArray[i + 1])  # inputArray 인덱스를 하나씩 올리면서 연산 값 number 배열에 추가
        result = max(number)    # result 변수에 number 배열 중 가장 큰 값 넣기

    print(result)   # 출력
