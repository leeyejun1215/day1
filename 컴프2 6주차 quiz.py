class person:
    def __init__(self, name, age, contact):
        self.name = name
        self.age = age
        self.contact = contact
    def info(self):
        print(f"회원님의 전화번호는{self.name} 나이는 {self.age} 연락처는 {self.contact} 입니다.")

name = input("이름을 입력하세요:")
age = input("나이를 입력하세요: ")
contact = input("연락처를 입력하세요 (예: 010-1234-5678): ")

person = person(name, age, contact)
person.info()
