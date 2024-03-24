# 사용자로부터 입력된 금액을 동전으로 교환하고자 할 때, 각 동전별 교환 개수 출력
# 동전의 총 개수가 최소가 될 수 있도록, 500->100->50->10원의 우선순위로 교환

def exchange(money):
    print("넣은 금액 : ", money, "원")
    w500 = money // 500
    money %= 500
    w100 = money // 100
    money %= 100
    w50 = money // 50
    money %= 50
    w10 = money //10
    print("500원 : ", w500, "개")
    print("100원 : ", w100, "개")
    print("50원 : ", w50, "개")
    print("10원 : ", w10, "개")

change_the_money = int(input("동전 교환기 : 얼마나 교환 하시겠습니까? "))
exchange(change_the_money)
