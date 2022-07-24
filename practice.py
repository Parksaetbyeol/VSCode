# Quiz 1) 당신은 cocoa 서비스를 이요하는 택시 기사. 
# 50명의 승객가 매칭 기회가 있을때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1:승객별 운행 소요 시간은 5~50분 사이의 난수로 정해진다.
# 조건2:당신은 소요 시간 5~15분 사이의 승객만 매챙해야 한다.

from random import *
count = 0 #총 탑승 승객 수
for i in range(1, 51): # 1~50 승객수
    time = randrange(5, 51) # 5~50분 소요시간
    if 5 <= time <= 15: # 소요시간 5~15분인 승객만 매칭
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        count += 1
    else: # 매칭 실패시
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0} 분".format(count))


# Quiz 2) 표준 체중을 구하는 프로그램을 작성하시오.
# 표준 체중: 각 개인의 키에 적당한 체중
# 남자 : 키(m) x 키 x 22 . 여: 키(m) x 키 x 21
# 조건1: 표준 체중은 별도의 함수 내에서 계산 (함수명:std_weight, 전달값:키(height),성별(gender))
# 조건2: 표준 체중은 소수점 둘째자리까지 표시

def std_weight(height,gender): # 키 m단위(실수), 성별 str
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175 # cm단위
gender = '남자'
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height,gender,weight))


# Quiz 3) 당신의 회사에서는 매주 1회 작성해야하는 보고서가 있습니다. 보고서는 항상 아래와 같이 출력되어야한다.
# - X 주차 주간보고 - 
# 부서 :
# 이름 :
# 업무 요약 :
# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
# 조건: 파일명은 '1주차.txt' 와 같이 만든다.

for i in range(1, 51):
    with open(str(i) + "주차.txt", 'w', encoding='utf8') as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :")


# Quiz 4) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.
# 예제
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print(self.location,self.house_type, self.deal_type, self.price, self.completion_year)

Houses = [] # 리스트 생성
house1 = House('강남', '아파트', '매매', '10억', '2010년')
house2 = House('마포', '오피스텔', '전세', '5억', '2007년')
house3 = House('송파', '빌라', '월세', '500/50', '2000년')
Houses.append(house1)
Houses.append(house2)
Houses.append(house3)

print('총 {0}대의 매물이 있습니다.'.format(len(Houses)))
for house in Houses:
    house.show_detail()