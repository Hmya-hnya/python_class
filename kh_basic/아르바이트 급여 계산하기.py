# 주간 근무 : 9860원
# 야간근무 : 주간 시급 * 1.5
# 주간근무 [1], 야간근무[2]를 입력 하세요 :
# 근무 시간을 입력해 주세요 :
# 입력한 시간 동안 근무한 주간 또는 야간 급여는 ___원 입니다.
# print(f"{근무시간}시간 동안 근무한 {근무타입문자열} 급여는 {급여}원 입니다.")


a = (input("주간근무[1], 야간근무[2]를 입력 하세요: "))
근무시간 = (input("근무 시간을 입력 해 주세요: "))
급여 =""

if a == 1:
    a = "주간근무"
    급여 = 근무시간 * 9860
    원환산 = f"{급여:,.0f}"
    print(f"{근무시간}시간 동안 근무한 {a} 급여는 {원환산}원 입니다.")
elif a == 2:
    a= "야간근무"
    급여 = 근무시간 * 9860 * 1.5
    원환산 = f"{급여:,.0f}"
    print(f"{근무시간}시간 동안 근무한 {a} 급여는 {원환산}원 입니다.")
else:
    print("근무타입을 잘못 입력 하였습니다.")
    exit()

"""
work_type = int(input("주간근무[1], 야간근무[2]를 입력 하세요: "))
work_time = int(input("근무 시간을 입력 해 주세요: "))
HOUR_PAY = 9860

if work_type == 1:
    pay = work_time * HOUR_PAY
elif:
    pay = work_time * HOUR_PAY * 1.5
else:
    print("근무 타입을 잘 못 입력 하였습니다.")
    exit()

work_type_str = work_type == 1 and "주간" or "야간"
pay_str = f"{pay:,.0f}"
print(f"{work_time}시간 동안 근무한 {work_type_str} 급여는 {pay_str}원 입니다.")
"""