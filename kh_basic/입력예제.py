# 사용자에게 콘솔로 입력을 받아 변수에 대입
# input() 함수를 사용
# input() 함수는 문자열로 입력을 받음
# 주석 단축키 Ctrl +/
from sphinx.cmd.build import jobs_argument

"""
print("이름을 입력 하세요: ", end="")
name = input()
print(f"당신의 이름은 {name} 입니다.")
"""
# 정수 타입으로 변수에 값을 대입하기 위해서는 형 변환이 필요
# 이름, 나이, 주소, 직업, 성적(실수 타입)을 입력 받아 출력 하기

# name = input("이름을 입력하세요: ")
# age = int(input("나이를 입력하세요: "))  #int: 정수
# addr = input("주소를 입력하세요: ")
# job = input("직업을 입력하세요: ")
# score = float(input("성적을 입력하세요: "))  #float: 실수

#print(f"안녕하세요? \"{name}\"님.") # 코드 내에서 "" 입력 원할 시 print(f'안녕하세요? "{name}"님.') 도 가능
#print(f"당신의 주소는 {addr}이고 직업은 {job}이고 나이는 {age}살 입니다.")
#print(f"당신의 성적은 {score:.2f}점 입니다.")

# 국어 영어 수학 과학 성적을 공백 기준으로 입력 받아 총점 구하기
"""
kor, eng, mat, scn = map(int, input("성적 입력: ").split()) #split: 쪼개기
print(f"총점 : {kor + eng + mat + scn}")
print(f"평균 : {(kor + eng + mat + scn)/4}")

score = list(map(int, input("성적 입력: ").split()))
print(f"총점: {sum(score)}")
print(f"평균: {sum(score) / len(score):.2f}") #len: 길이 함수 (요소의 갯수를 구함)
"""

# 24시간제 시간을 ':' 가준으로 입력 받아서 시, 분, 초로 찍는데 12시간제로 변환하여 출력하기
hour, min, sec = map(int, input("시:분:초 : ").split(":"))

if hour > 12:
    hour -= 12  # hour = hour =12
    print(f"오후 {hour}시 {min}분 {sec}초")
else:
    print(f"오전 {hour}시 {min}분 {sec}초")

