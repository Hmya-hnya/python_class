# 조건이 참인 동안 반복 수행
# n = int(input("정수 입력: "))
# sum = 0 # 값을 누적하기 위한 변수
# while n:  # Java에서는 성립하지 않음 (while n > 0 으로 입력 필요) // 다른 언어에서는 0이 아닌 모든 값은 참으로 간주
#     sum += n # sum = sum+n
#     n -= 1 # n= n-1
# print(sum)

# for i in range(1, n+1): # 범위 기반의 for문 (일정한 크기만큼~)
#     sum += i
# print(sum)

# while문은 주로 횟수가 정해지지 않은 반복적인 수행을 할 때 사용
"""
while True:  # 반복문 내에 탈출 조건이 있어야 함
    age = int(input("나이를 입력 하세요: "))
    if 0 <= age < 200: break # 정상적으로 값이 입력 되었으므로 반복문 탈출
    else: print("나이를 잘못 입력 하셨습니다.")

print(f"당신의 나이는 {age}살 입니다.")
"""
# for문은 정해진 범위 만큼을 반복 수행 할 때 효과적
# for (요소) in 시퀀스: 시퀀스 자료에 대한 자동 순회,
"""
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit, end=" ")

name = "asdf"
for e in name:
    print(e, end="-")

for e in input("문자열 입력: "):
    print(e, end="-")
"""

# for (인덱스) in range(시작값, 종료값, 증감값): 0부터 시작 생략/ 1부터 증가 생략 가능
# n = int(input("정수 값 입력: "))
# sum = 0
# for i in range(1, n+1, 1): # 시작값이 0 인 경우 생략 가능, 증감값이 1인 경우 생략 가능
#     sum += i
# print(sum)

# 이중 for 문 사용하기
# n = int(input("정수 입력: "))
# for i in range(0, n):  # 0~n 미만까지
#     print(f"i={i} |", end="")
#     for j in range(0, n):
#         print("*", end=" ")
#     print()

# 이중 for문 구구단 찍기
# for i in range(2, 10):
#     for j in range (1, 10):
#         print(f"{i} X {j} = {i*j}")
#     print("-"*15)

#제어문: break, continue
# break: 반복문을 탈출 할 때 사용
# continue: 아래의 문장을 수행하지 않고 반복문의 조건식으로 이동, (해당 루틴은 수행 된 걸로 간주)
# n = int(input("정수 입력: "))
# for i in range(n):
#     if i % 2 == 0: continue # 짝수이면 아래의 문장을 수행하지 않음
#     print(i)

# 반복문을 반대로 수행하기
# n = int(input("정수 입력: "))
# for i in range(n, 0 - 1, -1): #시작값, 최종값, 증감값
#     print(f"인덱스: {i}")

# for문으로 알파벳 출력하기
# ASCII (아스키코드에서 확장 된 것이 유니코드)
# chr(): 유니코드를 입력받아 그 코드에 해당하는 문자를 출력
# ord(): 문자의 유니코드값을 돌려주는 함수

for i in range(ord("A"), ord("z")+1):
    print(chr(i), end=" ")
print()

for i in range(65, 91):
    print(chr(i), end=" ")
print()

