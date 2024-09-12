# 제어문이란? 조건문과 반복문의 의미
"""
num =  int(input("정수값 입력: "))

if num > 100:
    print(f"{num}은 100보다 큰 수 입니다.")
elif num == 100:
    print(f"{num}은 100입니다.")
else:
    print(f"{num}은 100보다 작은 수 입니다.")
"""

# 실습문제
# 성적을 입력 받아서 0 ~ 100 사이가 아니면 성적을 잘못 입력하였다고 표기
# 성직이 0 ~ 100 사이이고, 90점 이상이면 A, 80점 이상이면 B, 70점 이상이면 C, 60점 이상이면 D, 그 외는 F

# num = int(input("성적을 입력하세요: "))

# if num >= 90 and num <= 100:
#     print("당신의 성적은 A 입니다.")
# elif num >= 80:
#     print("당신의 성적은 B 입니다.")
# elif num >= 70:
#     print("당신의 성적은 C 입니다.")
# elif num >= 60:
#     print("당신의 성적은 D 입니다.")
# elif num >= 0:
#     print("당신의 성적은 F 입니다.")
# else:
#     print("성적을 잘못 입력하였습니다.")
#--------------if문
# if 0 <= num <= 100:   #중첩 if문 // exit: 강제 종료
#     if num >= 90: print("A")
#     elif num >= 80: print("B")
#     elif num >= 70: print("C")
#     elif num >= 60: print("D")
#     else: print("F")
# else:
#     print("성적을 잘못 입력하였습니다.")
#------------While문

while True:
    num = int(input("성적을 입력하세요: "))
    if 0 <= num <= 100:
      if num >= 90: print("A")
      elif num >= 80: print("B")
      elif num >= 70: print("C")
      elif num >= 60: print("D")
      else: print("F")
      break
    else:print("성적을 잘못 입력하였습니다.")

# 세자리 정수 입력 받아 100의자리, 10의자리, 1의자리 로 나누어 담고
# 이 중 가장 큰 수 출력
# 몫과 나머지로 변수 할당
# if ~ else 값 비교

# n = int(input("세 자리 정수 입력: "))
# a = n // 100   #int(num[0])
# b = (n % 100) // 10  #int(num[1])
# c = (n % 100) % 10  #int(num[2]) -> 로도 가능
#
# if n<100 or n>999:
#     print("숫자를 잘못 입력하였습니다.")
# else:
#     if a > b:
#         if a > c: print(f"{a}이(가) 가장 큽니다.")
#         else: print(f"{c}이(가) 가장 큽니다.")
#     else:
#         if b > c: print(f"{b}이(가) 가장 큽니다.")
#         else: print(f"{c}이(가) 가장 큽니다.")
