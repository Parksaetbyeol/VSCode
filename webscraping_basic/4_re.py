# *--정규식 regular expression--*

import re
# 차량번호 abcd -> 기억하는건 ca?e

# *--정규식 사용 예제--*
# p(pattern)
p = re.compile("ca.e") 
# . : 하나의 문자를 의미 > ca.e = care, cafe, case... | caffe(X)
# ^ : 문자열의 시작을 의미 > ^de = desk, destination... | fade(X)
# $ : 문자열의 끝을 의미 > se$ = case, base... | face(X)

def print_match(m):
    if m:
        print("m.group():", m.group()) # 일치하는 문자열 반환
        print("m.string:", m.string) # 입력받은 문자열 반환
        print("m.start():", m.start()) # 일치하는 문자열의 시작 index
        print("m.end():", m.end()) # 일치하는 문자열의 끝 index
        print("m.span():", m.span()) # 일치하는 문자열의 시작과 끝 index
    else:
        print("매칭되지 않음")

m = p.match("careless") # match:주어진 문자열의 처음부터 일치하는지 확인(뒤에 less 붙어도 상관x)
print_match(m)
print(m.group()) # 매치되지 않으면 에러 발생함

m = p.search("good care") # search : 주어진 문자열 중에 일치하는지 확인
print_match(m)
 
lst = p.findall("good care cafe") # findall : 일치하는 모든 것을 리스트 형태로 반환
print(lst) # ['care', 'cafe'] 반환

# *--정리--*
# 1. re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 리스트 형태로 반환

# 원하는 형태 : 정규식
# . : 하나의 문자를 의미 > ca.e = care, cafe, case... | caffe(X)
# ^ : 문자열의 시작을 의미 > ^de = desk, destination... | fade(X)
# $ : 문자열의 끝을 의미 > se$ = case, base... | face(X)

# 추가공부
# w3schools
# python re검색 > docs 문서확인
