chars = 'happy'

# 1. 단순 순회 (for)
for char in chars:
    print(char)

# 2. 인덱스로 접근
for idx in range(len(chars)):
    print(idx, chars[idx])

for idx, value in enumerate(chars):
    print(idx, chars[idx])
