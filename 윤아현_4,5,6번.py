#!/usr/bin/env python
# coding: utf-8

# ### 4. NLTK 임포트하고, text4에서 4자리 단어만 출력하세요.

# In[27]:


from nltk.book import *
four_word = set([word for word in text4 if len(word) == 4]) # 중복을 제거하기 위해 set함수를 쓰고, 리스트 컴프리헨션을 써주었습니다.

print(four_word)


# ### 5. text7에서 가장 긴 단어는 몇 자 인가? 

# In[29]:


long_word = 0
for word in text7:
    if len(word) > long_word:
        long_word = len(word)
        
print(long_word)


# ### 6. 아래의 지문을 똑같이 출력하는 프로그램을 작성하시오. (한 줄에 한 문장씩 출력, 문자열 간격과 줄바꿈에 유의하여 작성)

# In[35]:


#과목명: 고급 파이썬 프로그래밍\Advanced Python programming
    #"이 수업은 금요일에 진행됩니다."
    
#수업은 실시간 강의로 진행됩니다.
    #- 질의사항은 조교에게 메일로 보내주세요
    
print('과목명: 고급 파이썬 프로그래밍/Advanced Python programming\n\t"이 수업은 금요일에 집행됩니다.\n\n수업은 실시간 강의로 진행됩니다.\n\t- 질의사항은 조교에게 메일을 보내주세요.')

