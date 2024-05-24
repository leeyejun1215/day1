class Bun:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.total = 0
    def sell(self):
        print(f"{self.name}을 {self.price}에 팔았습니다.")
        self.total += self.price
    def eat(self):
        print(f"{self.name}을 먹습니다.")

puff_Bun = Bun("슈크림", 1000)
puff_Bun.sell()
puff_Bun.sell()
puff_Bun.sell()
puff_Bun.sell()
print(puff_Bun.total)
