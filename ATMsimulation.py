##ATM시뮬레이터

##잔액확인 ,입출금 함수 만들기.

def checkbalance(bal) : 
    users[bal]
    




    
##사용자 로그인 dict 만들기
users = {
    "kim" :  {"password" : "1234"}
}

##로그인
user_id = input("아이디를 입력하세요 >> ")
while True :
    if user_id in users:
        pw = input("비밀번호를 입력하세요 >> ")
        
        if pw == users[user_id]["password"] :
            print(f'로그인 성공! {user_id}님 환영합니다.')
            print("")
            break
        else :
            print("입력오류")
    else :
        print("존재하지 않는 사용자입니다.")

## ATM파일 실행

while True :
    print (f'{user_id}님 [ATM에 오신걸 환영합니다.]')
    print("1. 잔액 확인")
    print("2. 입금")
    print("3. 출금")
    print("4. 종료")
    user_input = int(input(">> "))
    
    if user_input == 1 :
        print("[잔액확인]")

    

    elif user_input == 4 :
        print("***프로그램을 종료합니다.***")
        break

    else :
        print("잘못된 입력.")
