```python
for M in moves:
	if M == 0:
		position[0] = position[0] - 1

        if position[0] < 0:
            return None

    elif M == 3:
        position[1] = position[1] + 1

        if position[1] == N:
            return None

    elif M == 1:
        position[0] = position[0] + 1

        if position[0] == N:
            return None

    elif M == 2:
        position[1] = position[1] - 1

        if position[1] < 0:
            return None
```

> 좌표 이동 구현



```python
x = 0
y = 0
position = [0, 0]

for i in mat:
    x = 0
    for j in i:
        if j == 1:
            position = [x, y]
        x += 1    
    y += 1
```

> 현재 좌표 구하기