dust = int(input('미세먼지 농도를 입력하세요 : '))

if dust > 150 :
    print('매우 나쁨')
    if dust > 300 :
        print('실외 활동을 자제하세요.')
elif dust > 80 :
    print('나쁨')
elif dust > 30 :
    print('보통')
elif dust >=0:
    print('좋음')
else :
    print('값이 잘못 입력되었습니다.')
