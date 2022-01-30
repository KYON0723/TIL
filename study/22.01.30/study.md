```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, po1, po2):
        self.po1 = po1
        self.po2 = po2

        # 가로 , 세로의 길이 구하기
        ga = self.po1.x - self.po2.x
        se = self.po1.y - self.po2.y

        # 절대값 으로 변경
        if ga < 0:
            ga = ga * -1

        if se < 0:
            se = se * -1

        self.ga = ga
        self.se = se
	
    # 넓이 = 가로 * 세로
    def get_area(self):
        return self.ga * self.se
	
    # 둘레 = 2 * (가로 + 세로)
    def get_perimeter(self):
        return 2 * (self.ga + self.se)
	
    # 정사각형 판별(가로 = 세로)
    def is_square(self):
        if self.ga == self.se:
            return True
        
        else:
            return False
```

