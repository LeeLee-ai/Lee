#7
fruit = input('과일을 입력하시오:')
fruit2 = input('과일을 하나 더 입력하시오:')
number = input('떼어낼 문자 갯수를 입력하시오:')
print(fruit[0:int(number)] + fruit2[-int(number):])


