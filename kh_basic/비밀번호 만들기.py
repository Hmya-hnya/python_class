# 각 사이트의 비밀번호 만들기
# 규칙1 : http://naver.com에서 앞의 http:// 잘라내기
# 규칙2 : 처음 만나는 점(.) 이후는 제외
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자에 포함된 'o' 갯수 +글자에 포함된 'k' 갯수+ '!' + 자신의이니셜(예: 'jks')

# url = input("사이트: ")
# my_str = url.replace("http://", "") # 입력 받은 문자열에서 'http://' 잘라내기
# my_str = my_str[:my_str.index(".")] # 0에서부터 '.'의 인덱스 미만까지 슬라이싱
# pwd = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + str(my_str.count("k")) + "!" + "kkh"
# print("비밀번호: " + pwd)
"""
file_name = "password.txt"
f = open(file_name, "wt")  #원래 encoding? 해야함 (??) 비밀번호라 안해도 됨?
while True:
    url = input("사이트: ")
    if url == "exit": break  #종료를 원할 시 url 입력(break)
    my_str = url.replace("http://", "")
    my_str = my_str[:my_str.index(".")]
    pwd = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) \   #(\백슬래시: 줄바꿈)
    + str(my_str.count("k")) + "!" + "kkh"
    f.write(pwd + "\n")
f. close() #끝나면 닫음
"""

