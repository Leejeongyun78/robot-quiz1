# ============================================================
#  Part A. Python 문제 (50점)
#  - 문제 설명은 문제지.pdf 에 있습니다.
#  - 함수 이름, 클래스 이름, 매개변수는 바꾸지 마세요. (자동 채점됩니다)
#  - 결과는 print 가 아니라 반드시 return 으로 돌려주세요.
#  - pass 를 지우고 코드를 작성하세요.
#  - 다 풀고 나면  python3 python_quiz.py  로 실행해서
#    에러 없이 예시 결과가 나오는지 꼭 확인하세요.
# ============================================================


# ------------------------------------------------------------
# 문제 1. 배달비 계산 (8점)
# ------------------------------------------------------------
def delivery_fee(total, distance):
    if total >=30000:
        return total

    else:
        if distance >= 5:
            return total+5000
        elif distance >=2:
            return total+3000
        else:
            return total+2000


# ------------------------------------------------------------
# 문제 2. 운동장 이벤트 당첨자 찾기 (12점)
# ------------------------------------------------------------
def find_winners(numbers):
    for i in range(numbers):
        if numbers>=10 and numbers<=17:
            winners=[]
            winners.append[numbers+1]
            return winners


# ------------------------------------------------------------
# 문제 3. 주문 금액 계산 (12점)
# ------------------------------------------------------------
def order_total(menu, orders):
    totol=0
    for i in range(orders[1]):
        if orders[i][1] =="비빔우동":
            total += 7000
        elif orders[i][1] =="튀김우동":
            total += 8000
        elif orders[i][1] == "유부초밥":
            total += 4000
        else:
            print("메뉴에 없는 음식입니다.")

    if total>0:
        return(total,1)
    else:
        return(0,0)


# ------------------------------------------------------------
# 문제 4. 비빔우동 키오스크 2.0 (18점)
# ------------------------------------------------------------
# (1) 여기에 SoldOutError 클래스를 직접 만드세요.
class SoldOutError:
    def __init__(self):

        return ("매진되었습니다")



class UdonKiosk:
    PRICE = 7000  # 비빔우동 한 그릇 가격

    def __init__(self, stock):
        self.stock=stock
        self.sold=0
        return (self.stock,self.sold)

    def order(self, text):
        
        
        if self.stock >=0 and type(self.stock) == int:
            
            if self.stock==0:
                return SoldOutError()
            else:
                self.stock-=text
                self.sold+=text
                return (self.stock,self.sold)
            
        else:
            return ValueError()
                   

    def total_sales(self):
        return self.PRICE*self.sold


# ============================================================
#  아래는 확인용 코드입니다. 수정하지 않아도 됩니다.
#  python3 python_quiz.py 로 실행하면 문제지의 예시와 비교할 수 있습니다.
# ============================================================
def main():
    menu = {"비빔우동": 7000, "튀김우동": 8000, "유부초밥": 4000}
    try:
        print("문제 1 :", delivery_fee(12000, 3))            # 3000
        print("문제 2 :", find_winners([10, 20, 17, 9]))     # [1, 3]
        print("문제 3 :", order_total(menu, ["비빔우동", "유부초밥", "비빔우동", "돈까스"]))  # (18000, 1)
        kiosk = UdonKiosk(3)
        print("문제 4 :", kiosk.order("2"))                  # 14000
        print("문제 4 :", kiosk.stock, kiosk.sold)           # 1 2
        print("문제 4 :", kiosk.total_sales())               # 14000
    except Exception as e:
        print("에러 발생 :", type(e).__name__, e)


if __name__ == "__main__":
    main()
