from infix2Postfix import Infix2Postfix
from EvalPostfix import evalPostfix

infix1 = [ '8', '/', '2', '-', '3', '+', '(', '3', '*', '2', ')']
infix2 = [ '1', '/', '2', '*', '4', '*', '(', '1', '/', '4', ')']

postfix1 = Infix2Postfix(infix1)
postfix2 = Infix2Postfix(infix2)

result1 = evalPostfix(postfix1)
result2 = evalPostfix(postfix2)

print('  중위표기: ', infix1)
print('  후위표기: ', postfix1)
print('  계산결과: ', result1, end='\n\n')

print('  중위표기: ', infix2)
print('  후위표기: ', postfix2)
print('  계산결과: ', result2)