# Quiz1) 당신은 cocoa 서비스를 이요하는 택시 기사. 
# 50명의 승객가 매칭 기회가 있을때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1:승객별 운행 소요 시간은 5~50분 사이의 난수로 정해진다.
# 조건2:당신은 소요 시간 5~15분 사이의 승객만 매챙해야 한다.

from random import *
count = 0 #총 탑승 승객 수
for i in range(1, 51) # 1~50 승객
    time = randrange(5, 51) # 5~50분 소요시간
    if 5 <= time <= 15: # 소요시간 5~15분인 승객만 매칭
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        count += 1
    else: # 매칭 실패시
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0} 분".format(count))


