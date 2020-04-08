'''
FileName : day1_problem5-1.py
Coder : Song Ki Tae
'''

if __name__ == '__main__':

    with open("number.txt", "r", encoding="UTF8") as file_1:    # number.txt 파일 읽어오기
        if file_1 is None:      # file_1이 없으면,
            print("파일을 읽어오는데 실패했습니다.")      # 에러 메세지 출력
        else:       # file_1이 있다면,
            print("파일을 불러왔습니다.\n")      # 확인 메세지 출력
            result = []     # 배열 만들기
            for i in file_1:    # number.txt 파일의 줄 수만큼 반복
                result.append(f"{eval(i)}")     # 배열에 연산한 결과 집어넣기
            with open("answer.txt", "w", encoding="UTF8") as file_2:    # answer.txt 파일 만들기
                file_2.write(str(result))   # answer.txt 파일에 result 배열 내용 쓰기
                print("answer.txt 파일에 연산 결과를 저장했습니다.")      # 확인 사살
