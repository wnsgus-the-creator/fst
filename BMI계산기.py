## BMI 계산기를 만들어 보자.

def bmiC(u_weight, u_height) :
    if u_height > 3 :
        u_height = u_height / 100
        
        u_bmi = u_weight / (u_height ** 2)    
    return u_bmi
    
print("BMI 계산기")
u_height = int(input("자신의 키를 입력해주세요 : "))
u_weight = int(input("몸무계를 입력해주세요 :"))

u_bmi = bmiC(u_weight, u_height)
print("당신의 BMI 지수 >>", u_bmi)

## 해석

if u_bmi < 18.5 :
    print("저체중입니다.")
elif u_bmi < 22.9 :
    print("정상입니다.")
elif u_bmi < 24.9 :
    print("과체중입니다.")
elif u_bmi <29.9 :
    print("비만입니다.")
elif 30.0 < u_bmi :
    print("고도비만입니다.")