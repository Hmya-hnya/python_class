# 2개의 문자열을 포인터 변수 s와 k에, 양의 정수를 정수형 변수 n에 각각 전달받아
# s 문자열의 뒤 부분의 n개 문자를 k문자열 앞에 끼워 넣는 코드
#
# s: seoul
# k: korea
# n: 2
# result: ulkorea

s = input("s: ")
k = input("k: ")
n = int(input("n: "))

# print(s[-n:] + k)  #음수 값 입력이 가능 한 경우(파이썬만)
pos = int(len(s) - n)   #음수 값 입력이 안 될 경우
print(s[pos:] + k)

