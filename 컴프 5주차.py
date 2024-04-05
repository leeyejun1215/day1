score = input("성적을 입력하세요: ")
a = int(score)

if 71 <= a <= 100:
    grade = "A"
elif 41 <= a <= 70:
    grade = "B"
elif 11 <= a <= 40:
    grade = "C"
else :
    grade = "D"
print("당신의 학점은 "+ grade)
