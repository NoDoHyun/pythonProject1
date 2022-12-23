def arbeitnum(money):           #인자는 호출때 사용한 인자랑 이름달라도 자리만 맞으면 작동합니다
    if(money>1500000):
        arbeit1=money/1500000   #고용가능한 알바수 구하기,메인의 진짜 arbeit과 혼동 피하기 위해 1 붙임
        while(1):
            print("%d명 고용가능"%arbeit1)
            select=(int(input("고용할 알바수")))
            if(select<=arbeit1):
                return select       #고용가능수와 선택수가 같을경우 그만큼 리턴
            else:
                print("그만큼 고용하기엔 돈이 부족합니다")
    else:
        print("돈부족, 고용불가")


money5=1000
arbeit=arbeitnum(money5)
print("알바수:",arbeit)