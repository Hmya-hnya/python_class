#영어 소문자와 대문자로 이루어진 단어를 입력받은 위,
#대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는 프로그램을 작성하시오.
#for 문을 사용해야 함
#isLower(): 소문자이면 True, 아니면 False

#islower 이용
a = input("문자 입력: ")
for i in a:
    if i.islower() == True:
        print(i.upper(), end="")
    else:
        print(i.lower(), end="")
print(end="\n")
#isupper이용
b = input("문자 입력: ")
for i in b:
    if i.isupper() == True:
        print(i.lower(), end="")
    else:
        print(i.upper(), end="")
print(end="\n")
#바로 입력되는 방법(선생님 답)
rst = ""
for e in input("입력: "):
    if e.islower():
        rst += e.upper()  # rst= rst+e.upper()
    else:
        rst +=e.lower()  # rst= rst+e.lower()
print(rst)
