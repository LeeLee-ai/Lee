#4
word = input ('단어를 입력하시오:')
character = input ('변수에서 추출할 문자위치에 해당하는 문자를 입력하시오:')
print("word".find(character))
#5
word2 = input ('단어를 입력하시오:')
character2 = input ('뺄 문자의 위치를 입력하시오:')
word3 = (list(word2))
word3.pop(int(character2))
word4 = "".join(word3)
print(word4)
