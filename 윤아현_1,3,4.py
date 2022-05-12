#!/usr/bin/env python
# coding: utf-8

# ### 1. 세 수를 입력 받고 가장 큰 수를 찾는 코드를 작성하시오.
# 
# - 예: 12, 14, 15 입력 받았다면 15
# * 조건식을 위한 문제이기 때문에 max() 함수는 인정하지 않음.

# In[2]:


first_num = int(input('첫번째 숫자를 입력해주세요:'))
second_num = int(input('두번째 숫자를 입력해주세요:'))
third_num = int(input('세번째 숫자를 입력해주세요:'))

max = first_num

if max < second_num:
    max = second_num

if max < third_num:
    max = third_num

print(f'입력하신 숫자 중 가장 큰 숫자는 {max}입니다.')


# ### 2. 달팽이가 높이 350미터인 나무 막대를 올라간다.
# 
# - 조건1: 달팽이는 낮에 5미터 올라간다.
# - 조건2: 밤에는 2미터 미끄러진다.
# - 조건3: 정상에 올라간 후에는 미끄러지지 않는다.
# - 달팽이가 막대기 정상에 올라가려면 며칠이 걸리는지 코드를 짜서 프린트하시오.
# - (모든 리터럴은 변수에 담겨야 한다. 코드 및 정답을 모두 제출한다.)

# In[15]:


height = 350

daytime = 5
night = 2

days = 0
snail = 0

while True:
    # 낮에 달팽이가 올라감
    snail += daytime
    
    if snail >= height:
        days += 1
        break  
        
    # 밤에 달팽이가 떨어짐
    snail -= night
    days += 1

print(days)


# ### 3. 편의점 매출 계산
# 
# - 조건1: 총 매출 = (소비자가 - 원가) * 개수
# - 조건2: 5개 이상 구매 시 전체 물품의 15% 할인
#      (할인 적용 품목 범위는 둘다 가능함)
#      
# 
# - 한 고객이 다음과 같이 물건을 구입했다고 할 떄, 편의점의 매출을 계산하시오.
# - 출력 조건:
#      - 최대한 모든 리터럴을 변수에 담을 것.
#      - 출력값은 총 매출액(정수)
# -     비요뜨 삼각김밥 콜라 바나나 홈런볼
# -    원가 480 900 380 1050 770
# -    소비자가 1300 2500 800 3200 1500
# -    개수 3 5 6 2 4

# In[29]:


# 원가
biyott = 480
gimbap = 900
coke = 380
banana = 1050 
homerun = 770

# 소비자가 - 원가 = 이익
biyott_revenue = 1300 - 480
gimbap_revenue = 2500 - 900
coke_revenue = 800 - 380
banana_revenue = 3200 - 1050
homerun_revenue = 1500 - 770

sale_percent = 15

total = biyott_revenue * 3 + gimbap_revenue * 5 + coke_revenue * 6 + banana_revenue * 2 + homerun_revenue * 4
food_num = 3 + 5 + 6 + 2 + 4

if food_num >= 5:
    total *= ((100 - sale_percent) / 100)

# 총매출
print(str(f'편의점의 총 매출은 {total}입니다.')) 


# In[ ]:




