#입력이 5인 경우
# *
# **
# ***
# ****
# *****

a = int(input("갯수 입력: "))
for i in range(0,a,1):  # 행의 개수 결정
    for j in range(i+1):  # *의 개수 결정 / i가 0에서부터 시작하기 때문에 '+1" 필요
        print("*", end="")
    print()
