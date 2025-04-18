##ATM시뮬레이터

##입출금 함수 만들기.
def deposit() :
    print("\n[입금]")
    dp = int(input("입금할 금액 >> "))
    user_info[user_id]["balance"] += dp
    print(f'\n{user_id}님 {dp}원 입금되어, 현재 잔액 {user_info[user_id]["balance"]}원 \n')

def withdraw() :
    print("\n[출금]")
    wd = int(input("출금할 금액 >> "))
    if user_info[user_id]['balance'] >= wd :
        user_info[user_id]["balance"] -= wd
        print(f'{user_id}님 {wd}원 출금되어, 현재 잔액 {user_info[user_id]["balance"]}원 \n')
    else :
        print(f'\n{user_id}님의 잔고가 충분하지 않습니다.')

    
##사용자 로그인 dict 만들기
users = {
    "kim" : {"password" : "1234"}
}

##회원정보 dictinary
user_info =  {
    "kim" : {"balance" : 10_000}
}


##로그인
def login() :
    while True:
        user_id = input("아이디를 입력하세요 >> ")    
        if user_id in users:
            pw = input("비밀번호를 입력하세요 >> ")            
            if pw == users[user_id]["password"] :
                print(f'\n로그인 성공! {user_id}님 환영합니다.')
                print("")
                return user_id
            else :
                print("###입력오류###")
        else :
            print("\n존재하지 않는 사용자입니다.\n")
            break #로그인 실패
        print(" ")

##회원가입 함수
def sign_up():
    while True :
        print("\n[회원가입 하기]")
        user_id = input("새 id 입력 >> ")
        if user_id not in users :
            pw = input("새 패스워드 입력 >>")
            users[user_id] = {"password" : pw}
            user_info[user_id] = {"balance" : 0}
            print("\n회원가입 완료! \n")
            break
        else :
            print("\n이미 존재하는 아이디입니다.\n")
    return 0

##시작
while True :
    print("[ATM 시뮬레이션]")
    print("1.로그인")
    print("2.회원가입")
    print("3.종료")
    try:
        user_input = int(input(">> "))
    except ValueError:
        print("숫자만 입력하세요. \n")
        continue

    if user_input == 1 :
        user_id = login()
        if user_id in users :
            break
        else :
            continue

    elif user_input == 2 :
        sign_up() ##회원가입하기
    elif user_input == 3 :
        print("####시스템을 종료합니다.####")
        break
    else :
        print("잘못된 입력.")

## ATM파일 실행
while True :

    print (f'{user_id}님 [ATM에 오신걸 환영합니다.]')
    print("1. 잔액 확인")
    print("2. 입금")
    print("3. 출금")
    print("4. 종료")
    user_input = int(input(">> "))
    
    if user_input == 1 :
        print("\n[잔액확인]")
        print(f'{user_info[user_id]["balance"]}원\n')

    elif user_input == 2 :
        deposit()

    elif user_input == 3 :
        withdraw()

    elif user_input == 4 :
        print("\n\n\n###시스템을 종료합니다.###")
        break
    else :
        print("잘못된 입력.")
