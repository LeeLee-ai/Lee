import re
voca = '\w+l'
vocabularies = input('단어 열개를 입력하시오:')
result = re.findall(voca, vocabularies)
print(result)
