# 문자열: 문자로 이루어진 데이터의 집합
# "", '', """ """, ''' '''
# 인덱싱: 시퀀스(리스트, 튜플, 문자열, input()) 자료형에서 특정 위치의 요소를 선택하는 작업
# 인덱싱은 0 부터 시작
# 슬라이싱: 시퀀스 자료형에서 일부 데이터를 추출하는 것 (잘라내는 것)
"""
jumin = input("주민등록번호 입력: ")    # 991120-1234567

#인덱싱
gender = jumin[7]
if gender == "1" or gender == "3" :
    print("남성입니다.")
else:
    print("여성입니다.")

# 태어난 년도를 구하기 위해서 슬라이싱
year = jumin[0:2] # 0이상 2미만 (0이 첫번째 자리 수), 0에서부터 시작되는 경우는 생략 가능
year = int(year)
if gender == "1" or gender == "2" :
    year +=1900
else:
    year +=2000

print(f"태어난 년도: {year}")

#생일 출력
mon = jumin[2:4]
day = jumin[4:6]
mon = int(mon)
day = int(day)
print(f"생일은 {mon}월 {day}일 입니다.")

#생년월일
print("생년월일: " + jumin[:6])
print("뒤 7자리: " + jumin[7:]) #7에서부터 끝까지
print("뒤 7자리: " + jumin[-7:]) #뒤 7자리부터 끝까지 (뒤부터 세는게 빠를 때 사용), -1은 맨 뒤의 자리

# print(jumin[14]) #String index out of range
"""
life = "Life is too short, You need Python"
tmp = life[0] + life[1] + life[2] + life[3]
print(tmp)

# 대소문자 바꾸기: upper(), lower()
a = "Hello Python Program..."
print(a.upper()) #모두 대문자
print(a.lower()) #모두 소문자

# 대문자-> 소문자, 소문자-> 대문자 ?? (오후에. 2024. 09. 11)

# 문자열 변경: replace("기존 문자열", "바꿀 문자열")

b = "Hello Python Program..."
n_b = b.replace("Python", "JavaScript")  # 변경할 문자열이 여러개여도 모두 변경됨
print(n_b)

# 문자열에 포함 된 문자 갯수세기 및 문자열 길이 구하기:
# count(): 갯수 세기 / 문자열 내장 함수로 문자열에 포함된 갯수
# __len__(): 문자열 길이를 반환
# len(): 문자열 길이를 반환
c = "Hello Python Program..."
print(c.count("l")) # 해당 문자열에서 매개변수로 전달한 문자/문자열 갯수를 반환
print(c.__len__()) # 문자열 길이 반환 -> 해당 건은 내장 함수로 문자열의 길이를 반환함
print(len(c))  # 문자열 길이 반환 -> 해당 건은 별도의 함수로 길이를 반환함

# 문자열 찾기: find(), rfind(), index()
# find(): 찾은 문자열의 첫 번째 인덱스를 반환 (찾지 못할 경우 -1)
# index(): 찾은 문자열의 첫 번째 인덱스를 반환 (찾지 못할 경우 ValueError 발생하고 종료)
# rfind(): 뒤에서부터 문자열을 찾음(reverse), 찾은 문자열의 인덱스는 앞에서부터 계산함.

phrase = "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점 찾기, 가장 좋은 선물은 용서"
print(phrase. find("가장"))
print(phrase. rfind("가장")) #뒤에서부터 찾지만 인덱스를 앞에서 부터
print(phrase. index("포기"))

print(phrase. find("나에게")) #-1
# print(phrase. index("나에게")) #substring not found
new_phrase = phrase.replace("가장", "나에게")
print(new_phrase)

# 문자열 연산자: +, *
print("태양고" + "나희도")
print("!"*10)
list = [0] * 10
print(list)

# 문자열의 양 옆의 공백제거: strip()
d = """
        안녕하세요.
        문자열의 공백을 제거  하겠습니다.
        여러개의 공백 치기       
"""
print(d.strip())

