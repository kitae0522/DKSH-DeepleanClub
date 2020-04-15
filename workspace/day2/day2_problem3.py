'''
FileName : day2_problem3.py
Coder : Song Ki Tae
'''


def palindrome(word):

    for i in range(len(word) // 2):  # 문자열 길이의 반만큼 반복
        if word[i] != word[-1 - i]:  # 왼쪽 문자와 오른쪽 문자를 비교하여 문자가 다르면
            return False  # 팰린드롬 문자가 아니다
        else:
            return True  # 팰린드롬 문자이다


if __name__ == '__main__':

    word = "level"
    res = palindrome(word)
    print(res)