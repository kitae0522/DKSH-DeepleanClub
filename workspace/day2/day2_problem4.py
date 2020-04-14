'''
FileName : day2_problem4.py
Coder : Song Ki Tae
'''

if __name__ == '__main__':

    userID = ["apple"]
    userDB = {userID[0] : "1234"}
    userMoney = {userID[0] : 0}

    while True:
        print("안녕하세요 농협은행입니다.\n"
              "원하는 서비스를 입력하세요\n"
              "① 로그인 ② 회원가입 ③ 나가기\n")
        answer = int(input(">>> "))

        if answer == 3:
          break

        elif answer == 1:
            log_input_id = input("아이디를 입력하세요 : ")
            log_input_pw = input("비밀번호를 입력하세요 : ")

            if log_input_pw != userDB[log_input_id]:
                print("로그인 실패")
                break

            elif log_input_pw == userDB[log_input_id]:
                while True:
                    print("원하시는 서비스를 선택하세요.\n"
                          "① 입금 ② 출금 ③ 이체 ④ 로그아웃\n")
                    service_input = int(input(">>> "))

                    if service_input == 4:
                        break

                    elif service_input == 1:
                        print("얼마를 입금하시겠습니까? (현재 통장에 있는 금액 : {}원)\n".format(userMoney[log_input_id]))
                        des_input = int(input(">>> "))

                        userMoney[log_input_id] += des_input
                        print("입금을 완료했습니다. (현재 통장에 있는 금액 : {}원)".format(userMoney[log_input_id]))

                    elif service_input == 2:
                        print("얼마를 출금하시겠습니까? (현재 통장에 있는 금액 : {}원)".format(userMoney[log_input_id]))
                        withdraw_input = int(input(">>> "))
                        if userMoney[log_input_id] - withdraw_input < 0:
                            print("출금 할 수 없습니다.")
                        else:
                            userMoney[log_input_id] -= withdraw_input
                            print("출금을 완료했습니다. (현재 통장에 있는 금액 : {}원)".format(userMoney[log_input_id]))

                    elif service_input == 3:
                        print("얼마를 누구한테 보내시겠습니까? (현재 통장에 있는 금액 : {}원)\n"
                              "(보낼 수 있는 상대 : {})\n"
                              "(입력 예시 : 1000 apple)".format(userMoney[log_input_id], userID))
                        trans_input, who = input(">>> ").split()
                        trans_input = int(trans_input)
                        if userMoney[log_input_id] - trans_input < 0:
                            print("이체 할 수 없습니다.")
                        else:
                            userMoney[log_input_id] -= trans_input
                            print("{}에게 {}원을 성공적으로 보냈습니다. (현재 통장에 있는 금액 : {}원)".format(who, trans_input, userMoney[log_input_id]))
                            userMoney[who] = trans_input

        elif answer == 2:
            reg_input_id = input("아이디를 입력하세요 : ")
            if reg_input_id in userID:
                print("이미 가입된 아이디입니다.")
                break

            elif reg_input_id not in userID:
                reg_input_pw = input("비밀번호를 입력하세요 : ")
                reg_input_pw_re = input("비밀번호를 다시 입력하세요 : ")
                if reg_input_pw == reg_input_pw_re:
                    userID.append(reg_input_id)
                    userDB[reg_input_id] = reg_input_pw
                    userMoney[reg_input_id] = 0
                    print("회원가입이 완료되었습니다.")
                elif reg_input_pw != reg_input_pw_re:
                    print("비밀번호가 서로 다릅니다.")