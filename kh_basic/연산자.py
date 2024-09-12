# 프로그램에서 값을 연산해야 하는 경우 사용
# 산술 연산자: +, -, *, /, //(몫-Java에는 없음), %(나머지), **(제곱)
"""
i = 10
j = 3
print(i + j)
print(i - j)
print(i * j)
print(i / j)
print(i // j) # 몫 구하기
print(i % j) # 나머지 구하기, 알고리즘 문제를 풀기 위해서 많이 나옴
print(i ** j) # 10^3
"""

#세율 구하기
"""
TAX_RATE = 0.10 #세율
income = int(input("당신의 수입은 얼마 입니까? "))
print(f"당신이 내야 할 세금은 {income * TAX_RATE} 원 입니다.")
"""

# 대입 연산자: 값을 변수에 대입 '='
# 복합 대입 연산자의 종류: +=, -=, *=, /=, //=, %=
num1 = 10
num1 += 2  #num1 = num1+2
print(num1) #12
num1 -= 10
print(num1) #2
num1 *= 2
print(num1) #4
num1 /= 4
print(num1) #1

# 비교 연산자: 두 개의 값을 비교해서 참/거짓을 만들어 냄
# '==' 같다, '>' 왼쪽이 크다, '>=' 왼쪽이 크거나 같다, '<', '<=', '!=' 같지 않다
a = 10
b = 20
print(a > b)
print(a < b)
print(a == b)
print(a >= b)
print(a >= b)
print(a != b) # 같지 않다

# 관계 연산자: and, or, not(이전 상태 부정) (in Java &&, \\, !)
x = 10
y = 20
z = 30
rst1 = (x > 0) and (x > y) # False
rst2 = (x > 0) or (x > y) # True
rst3 = not((x > 0) or (x > y)) # False
print(rst1, rst2, rst3)

# 3항 연산자: 항이 3개인 연산자 (참과 거짓이 있는 조건문과 동일) -> (조건) and '참' or '거짓' /
# if문보다 코드가 간결함, switch case? 제약은 있지만 코드가 더 빠르고 간결함 (고정된 뭐시기...)
age = int(input("나이를 입력 하세요: "))

# is_adult = age > 19 and "성인" or "미성년자"
# print(f"당신은 {is_adult} 입니다.")
#if문 예시 -> 3항 연산자보다 길고 복잡함
# if age > 19:
#     print(f"당신은 성인 입니다.")
# else:
#     print(f"당신은 미성년자 입니다.")
is_adult = True if age > 18 else False
print(1) if age > 18 else print(-1)

age > 19 and print("성인입니다.") or print("미성년자 입니다.")
is_adult = age > 19 and "성인" or "미성년자"

#뭔소리야