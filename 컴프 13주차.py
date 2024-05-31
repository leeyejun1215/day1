class Beverage:
    menu = {"커피": 3000, "녹차": 2500, "아이스티": 3000}

    def calculate(self, name, quantity):
        if name in self.menu:
            price = self.menu[name] * quantity
            print(f"{name} {quantity}잔의 가격은 {price}원 입니다.")
        else:
            print("죄송합니다. 해당 음료는 메뉴에 없습니다.")

def main():
    kiosk = Beverage()
    while True:
        order = input("주문할 음료를 입력하세요 (종료하려면 '종료' 입력): ")
        if order == '종료':
            break
        quantity = int(input("수량을 입력하세요: "))
        kiosk.calculate(order, quantity)

if __name__ == "__main__":
    main()
