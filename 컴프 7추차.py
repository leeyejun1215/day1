numbers = [[1,2,3], [4,5,6], [7,8,9]]
result = []

for row in numbers:
    for num in row:
        if num % 2 == 0:
         result.append(num)
print('짝수를 출력하겠습니다:',result)
