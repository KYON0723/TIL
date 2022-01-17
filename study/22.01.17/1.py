dust = int(input(미세먼지 농도를 입력하세요 : ))

if dust > 150 :
    print('매우 나쁨')
elif dust > 80 :
    print('나쁨')
elif dust > 30 :
    print('보통')
else :
    print('좋음')
