'''
FileName : day1_problem5.py
Coder : Song Ki Tae
'''

if __name__ == '__main__':

    num1 = int(input("원하는 숫자를 입력하세요 : "))   # num1 변수에 첫번째 숫자 입력
    oper = input("연산자를 입력하세요(+, -, *, /) : ")   # oper 변수에 연산자 입력
    num2 = int(input("원하는 숫자를 입력하세요 : "))   # num2 변수에 두번째 숫자 입력

    if oper == "+":     # 만약 연산자가 +일때,
        result = num1 + num2    # num1 + num2 를 result라는 변수를 만들어 저장
    elif oper == "-":   # 만약 연산자가 +일때,
        result = num1 - num2    # num1 - num2 를 result라는 변수를 만들어 저장
    elif oper == "/":   # 만약 연산자가 +일때,
        result = num1 / num2    # num1 / num2 를 result라는 변수를 만들어 저장
    elif oper == "*":   # 만약 연산자가 +일때,
        result = num1 * num2    # num1 * num2 를 result라는 변수를 만들어 저장
    else:
        print("잘못된 접근입니다.")

    print("결과는 {}입니다.".format(result))      # 결과를 format 메소드를 사용하여 출력
