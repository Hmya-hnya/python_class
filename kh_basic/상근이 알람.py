# 상근이 알람: 입력 시간보다 45분 일찍 알람 설정하기
# 입력: 시간과 분을 입력받음, 24시간제
# 하루의 시작은 0:0, 끝은 23:59, 불필요한 0은 사용하지 않음

# 입력은 H, M을 ":"기준으로 입력
# 시간을 분으로 환산하기
# 분으로 환산한 시간이 45보다 작으면 시간을 별도 계산해야 함
# 45분을 빼줌
# 다시 시간과 분으로 환산하여 출력

# while True:
#     H, M = map(int, input("시:분 : ").split(":"))
#     if 0 <= H < 24 and 0 <= M < 60: break
#     else: print("시간을 잘못 입력하였습니다.")
#
# 설정시간 = int((int(H) * 60 + int(M) - 45))
#
# if 설정시간 >= 0:
#     print(f"{설정시간//60}:{설정시간%60}")
# elif 설정시간 < 0:
#     전날 = int(설정시간 + (24*60))
#     print(f"{전날//60}:{전날%60}")

while True:
    h, m = map(int, input("시간 입력: ").split(":"))
    if 0 <= h < 24 and 0 <= m < 60: break
    else: print("시간을 잘못 입력 하였습니다.")

calc_min = h * 60 + m #입력 받은 시간을 분으로 환산
if calc_min < 45:
    calc_min = 24 * 60 + m  # else문은 필수가 아님
calc_min -= 45
print(f"{calc_min // 60}:{calc_min % 60}")

