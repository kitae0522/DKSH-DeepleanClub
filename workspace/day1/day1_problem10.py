'''
FileName : day1_problem10.py
Coder : Song Ki Tae
'''

# Q1
# 홍길동씨의 과목별 점수는 다음과 같다. 홍길동씨의 평균 점수를 구해 보자.
# 국어 80 영어 75 수학 55
print("평균 점수 : {}".format((80 + 75 + 55) / 3))

# Q2
# 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법에 대해 말해 보자.
num = 13
if num % 2 == 0:
    print("짝수")
elif num % 2 != 0:
    print("홀수")

# Q3
# 홍길동씨의 주빈등록번호는 881320-10608234이다.
# 홍길동씨의 주민등록번호를 연원일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.
pin = "881320-10608234"
yyyymmdd = pin[0:6]
num = pin[7:]
print(yyyymmdd)
print(num)

# Q4
# 주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다.
# 주민등록번호에서 성별을 나타내는 숫자를 출력해 보자.
pin = "881320-30608234"
gender = int(pin[7])
if gender == 1:
    print("남자입니다.")
elif gender == 2:
    print("여자입니다.")
else:
    print(gender)

# Q5
# 다음과 같은 문자열 a:b:c:d가 있다.
# 문자열의 replace 함수를 사용하여 a#b#c#d로 바꿔서 출력해 보자.
string = "a:b:c:d"
replace_string = string.replace(":", "#")
print(replace_string)

# Q6
# [1, 3, 5, 4, 2]라는 리스트를 [5, 4, 3, 2, 1]로 만들어보자.
num_list = [1, 3, 5, 4, 2]
num_list.sort()
num_list.reverse()
print(num_list)

# Q7
# ['Life', 'is', 'too', 'short'] 라는 리스트를 Life is too short라는 문자열로 만들어 출력해 보자.
str_list = ['Life', 'is', 'too', 'short']
result = " ".join(str_list)
print(result)

# Q8
# (1,2,3)이라는 튜플에 4라는 값을 추가하여 (1,2,3,4)처럼 만들어 출력해 보자.
num_tuple = (1, 2, 3)
num_tuple = num_tuple + (4,)
print(num_tuple)

# Q9
# 다음과 같은 딕셔너리 a가 있다.
# 다음 중 오류가 발생하는 경우는 어떤 경우인가? 그리고 그 이유를 설명해 보자.
'''
답은 3번 a[[1]] = 'python'이다.
이유는 [1]는 딕셔너리는 튜플같이 변할 수 있는 값을 사용할 수 없기 때문이다.
'''

# Q10
# 딕셔너리 a에서 'B'에 해당되는 값을 추출해 보자.
a = {"A": 90, "B": 80, "C": 70}
result = a.pop("B")
print(a)
print(result)

# Q11
# a 리스트에서 중복된 숫자들을 제거해 보자.
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)

# Q12
# 파이썬은 다음처럼 동일한 값에 여러 개의 변수를 선언할 수 있다.
# 다음과 같이 a, b 변수를 선언 한 후 a의 두 번째 요솟값을 변경하면 b의 값은 어떻게 될까?
# 그리고 이런 결과가 나오는 이유에 대해서 설명해 보자.
'''
[1, 4, 3]이 나온다.
이유는 a = b이기 때문이다
'''
