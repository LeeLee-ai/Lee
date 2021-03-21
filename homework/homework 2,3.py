#2 
strings = input ('enter a string:')
print(strings * 2)
#3
String = input('문자를 입력하시오:')
number = input('숫자를 입력하시오:')
if int(len(String)) >= int(number):
    print(String[-int(number):])
else:
    print(String[::-1])