# 세 자리 자연수 A, B, C
# ex. A= 150, B = 266, C= 427 의 곱은 17037300
# 숫자 0~9의 갯수 세기
"""
while True:
    A, B, C = map(int, input("세 자리 자연수 3개 입력: ").split(" ")) # 숫자를 공백 기준으로 입력 받음
    if 100<=A<=999 and 100<=B<=999 and 100<=C<=999: break
    else: print("숫자를 다시 입력 해 주세요")

num = str(A * B * C)  # 숫자를 문자열로 변환
print(f"A*B*C= {num}")

for i in range(1,10,1):
    if num.count(str(i)) == 0: continue
    print(f"{i}의 갯수: " ,num.count(str(i)),"개")
print("*0개인 수는 노출되지 않음")
"""

# 실습 2번: 문자열 반전, 문자열을 입력 받아서 문자열 반전 출력
# ex. ABCDEF => FEDCBA
"""
a = input("문자열을 입력: ")
re_a=""
for i in a:
    re_a = 
print(re_a)
"""
in_str = input("문자열 입력: ")
#방법1
for i in range(len(in_str)-1, -1, -1):  # 5부터 시작해야 하는데 len으로 도출 시 5부터 시작하게 되므로 '-1'을 함
    print(in_str[i], end="")
#방법2
reverse_str = in_str[::-1]
print(reverse_str)