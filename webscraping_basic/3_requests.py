import requests

res = requests.get("http://naver.com")
# res = requests.get("http://nadocoding.tistory.com")

print("응답코드 :", res.status_code) # 200이면 정상 작동


# *-- 정상작동하는지 확인 --*
# if res.status_code == requests.codes.ok: # == 200
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드", res.status_code, "]")

# *-- 정상작동하는지 확인2 --*
res.raise_for_status()
print("웹 스크래핑을 진행합니다") # 오류가 나면 프로그램 종료함

# 실습
res = requests.get("http://google.com") # 원하는 페이지 접속
res.raise_for_status() # 페이지 접속 확인
print(len(res.text)) # 페이지 길이 확인
# print(res.text) # 페이지 텍스트 확인 (너무 기니까 파일로 가져와서 보자)

# 파일로 가져와서 열어보면 google페이지 열림
with open("mygoogle.html",'w', encoding='utf-8') as f:
    f.write(res.text)



