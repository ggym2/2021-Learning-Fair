#변수 및 리스트
korea = ['부대찌개', '제육볶음', '비빔밥', '김치찌개', '된장찌개', '육개장', '돼지국밥', '경양식돈까스', '찜닭', '순대국밥', '소고기장터국밥', '닭갈비', '낙지볶음', '순두부찌개', '설렁탕', '족발', '보쌈', '닭발', '오징어볶음', '김치찜', '추어탕', '돌솥비빔밥']
western = ['파스타', '피자', '리조또', '까르보나라', '아란치니', '스테이크', '햄버거', '뉴욕핫도그', '샐러드', '스프', '타코']
japan = ['회', '초밥', '돈부리', '라멘', '가츠동', '일식돈까스', '대창덮밥', '연어덮밥', '오꼬노미야끼', '우동', '야끼소바', '스키야키']
china = ['짜장면', '짬뽕', '볶음밥', '마라탕', '꿔바로우', '짬뽕밥', '양꼬치', '잡채밥', '울면']
school = ['떡볶이', '김밥', '쫄면', '만두', '토스트', '라면', '핫도그', '샌드위치']
asian = ['쌀국수', '똠양꿍', '분짜', '팟타이', '푸팟퐁커리']
idn = korea + western + japan + china + school + asian
group = [korea, western, japan, china, school, asian]
name=["한식","양식","일식","중식","분식", "아시안"]
mate={1:korea,2:western,3:japan,4:china,5:school,6:asian, 7:idn}
matemenu={1:"한식",2:"양식",3:"일식",4:"중식",5:"분식", 6:"아시안"}


#함수 불러오기
import random


#함수 선언
def reco():
    return random.randrange(0,b)


#프로그램 코딩
print("직장인들의 최고의 난제! 점심이 고민되신다고요?")
print("그럴 땐 점심메뉴추천기 이름하야 점.메.추! 이용해보시는건 어떠세요?")
print("\n< PRESS ONLY NUMBERKEY + ENTER >")

while True :
    print("\n============================================")
    print("\n원하시는 메뉴를 선택해주세요")
    start=int(input("\n1. 시작하기    2. 메뉴관리하기    3. 종료하기 \n\n"))

    if start != int(1) and start != int(2) and start != int(3):
        print("\n숫자 1, 2, 3 중 한가지를 골라, 입력해주세요.")

    # 1. 시작하기 - 음식메뉴 추천
    
    if start == 1:
        print("\n============================================")
        print("\n그럼 시작해볼까요!")
        print("어떤 종류의 음식을 먹고싶나요?")
        choice=int(input("\n1. 한식   2. 양식   3.일식   4. 중식   5. 분식   6. 아시안  7. 잘 모르겠어요 \n\n"))

        while choice != int(1) and choice != int(2) and choice != int(3) and choice != int(4) and choice != int(5) and choice != int(6) and choice != int(7) :
            print("\n숫자 1~7 중 한가지를 골라, 입력해주세요.")
            choice=int(input("\n1. 한식   2. 양식   3.일식   4. 중식   5. 분식   6. 아시안  7. 잘 모르겠어요 \n\n"))

        b=len(mate.get(choice))
        a=reco()
        if choice == 7 :
            print("\n그럼 제가 아무거나 추천해볼게요!")
        print("\n오늘 점심에는 ["+ mate.get(choice)[a] + "] 어떠신가요?")
        print("메뉴가 마음에 드시나요?\n")
        last=int(input("1. 네! 고마워요 점메추!    2. 아니오ㅠㅠ\n\n"))
        while last != 1 :
            a=reco()
            if last != int(1) and last != int(2) :
                print ("\n숫자 1, 2 중 한가지를 골라, 입력해주세요.")
                print("메뉴가 마음에 드셨나요?\n")
                last=int(input("\n1. 네! 고마워요 점메추!    2. 아니오ㅠㅠ\n\n"))
            else :
                print("\n============================================")
                print("\n다시 추천 드려볼게요 그럼 [" + mate.get(choice)[a]+ "] 어떠신가요?")
                print("메뉴가 마음에 드시나요?\n")
                last=int(input("1. 네! 고마워요 점메추!    2. 아니오ㅠㅠ\n\n"))
        print("\n\n그럼 맛있는 점심식사 되세요!")
        print()
        

    # 2. 메뉴관리하기
    elif start == 2 :
        print("\n============================================")
        print("\n메뉴리스트를 보거나 원하시는 메뉴를 추가/삭제할 수 있어요!")
        print("무엇을 도와드릴까요? \n")
        pick=int(input("1. 메뉴 확인   2. 메뉴 추가하기   3. 메뉴 삭제하기   4. 처음으로 돌아가기 \n\n"))

        while pick != 4 :
            # 2-1. 메뉴확인
            if pick == 1 :
                print("\n\n모든 메뉴를 보여드립니다\n")
                b=len(group)
                for i in range(0,b) :
                    print("%s → "%name[i],end='')
                    c=len(group[i])
                    f=group[i]
                    for k in range(0,c) :
                        print("  %s  "%f[k],end='')
                        if (k+1) %5 == 0 :
                            print("\n\n       ",end = '') 
                    print("\n")
                print("\n\n이 외 더 도와드릴게 있나요? \n")

            # 2-2. 메뉴 추가
            elif pick == 2 :
                print("\n어떤 종류의 메뉴를 추가하실 건가요?")
                plus = int(input("\n1. 한식   2. 양식   3.일식   4. 중식   5. 분식   6. 아시안 \n \n"))
                while plus != int(1) and plus != int(2) and plus != int(3) and plus != int(4) and plus != int(5) and plus != int(6) :
                    print("\n숫자 1~6 중 한가지를 골라, 입력해주세요.")
                    plus=int(input("\n1. 한식   2. 양식   3.일식   4. 중식   5. 분식   6. 아시안 \n \n"))
                
                print("\n[%s]에 어떤 메뉴명을 추가할까요?\n" %matemenu.get(plus))
                h=mate.get(plus)
                add=str(input())
                h.append(add)
                print("\n\n[%s]에 %s 메뉴를 추가하였습니다!"%(matemenu.get(plus),add))
                print("\n============================================\n")
                print("%s  → "%matemenu.get(plus), end='')
                b=len(mate.get(plus))
                for i in range(0,b) :
                    print("  %s  "%h[i],end='')
                    if (i+1) %5 == 0 :
                        print("\n\n       ",end = '')
                print("\n \n============================================")
                print("\n\n이 외 더 도와드릴게 있나요? \n")

            # 2-3. 메뉴 삭제
            elif pick == 3 :
                print("\n어떤 종류의 메뉴를 삭제하실 건가요?")
                erase = int(input("\n1. 한식   2. 양식   3.일식   4. 중식   5. 분식    6. 아시안  \n \n"))

                while erase != int(1) and erase != int(2) and erase != int(3) and erase != int(4) and erase != int(5) and erase != int(6) :
                    print("\n숫자 1~6 중 한가지를 골라, 입력해주세요.")
                    erase=int(input("\n1. 한식   2. 양식   3.일식   4. 중식   5. 분식   6. 아시안 \n \n"))
                
                print("\n[%s]에 어떤 메뉴명을 삭제할까요?\n" %matemenu.get(erase))
                b=len(mate.get(erase))
                h=mate.get(erase)
                for i in range(0,b) :
                    print("%s  "%h[i],end='')
                    if (i+1) %5 == 0 :
                        print("\n\n",end = '')
                back=str(input("\n\n"))
                while h.count(back) == 0:
                    print("\n해당 메뉴명이 없습니다. 공백과 오타에 주의하여 다시 입력해주세요.")
                    back=str(input("\n\n"))
                h.remove(back)
                print("\n\n[%s]의 %s 메뉴를 삭제하였습니다!"%(matemenu.get(erase),back))
                print("\n============================================\n")
                print("%s  → "%matemenu.get(erase), end='')
                b=len(mate.get(erase))
                for i in range(0,b) :
                    print("  %s  "%h[i],end='')
                    if (i+1) %5 == 0 :
                        print("\n\n         ",end = '')
                print("\n \n============================================")
                print("\n\n이 외 더 도와드릴게 있나요? \n")

            else :
                print("\n숫자 1, 2, 3, 4 중 한가지를 골라, 입력해주세요.\n")
                

            pick=int(input("1. 메뉴 확인   2. 메뉴 추가하기   3. 메뉴 삭제하기   4. 처음으로 돌아가기 \n\n"))
        print()
        
    # 3. 종료하기
    elif start == 3 :
        print("\n============================================")
        print("\n이용해 주셔서 감사합니다!")
        print("\n============================================\n")
        break

