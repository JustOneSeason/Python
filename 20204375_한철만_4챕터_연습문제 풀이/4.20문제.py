from ArrayStack import ArrayStack
from infix2Postfix import Infix2Postfix
from EvalPostfix import evalPostfix


infix = input("중위 표기법으로 수식을 입력하세요: ")
infix_tokens = infix.replace(" ", "")
postfix = Infix2Postfix(infix_tokens)
result = evalPostfix(postfix)

print("중위 표기법:", infix_tokens)
print("후위 표기법:", postfix)
print("계산 결과:", result)





