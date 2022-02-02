```python
import random
    
# list 정보를 저장
def __init__(self, li):
        self.li = li
    
# list에서 n개 만큼 뽑아서 출력
def pick(self, n):
	result = ClassHelper.random.sample(self.li, n)
    print(result)
    
# list에서 2개씩 뽑아서 조를 지음
def match_pair(self):
    newli = self.li

    # 3명 이하로 남을 때 까지 2명씩 뽑음
    while len(newli) > 3:
    	result = ClassHelper.random.sample(newli, 2)
        print(result)
            
        뽑힌 2명은 list에서 제거
        newli = [i for i in newli if i not in result]
        
# 마지막 남은 인원(2~3명) 출력
print(newli)
```

