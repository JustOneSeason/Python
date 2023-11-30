from ArrayStack import ArrayStack

def checkBrackets(input_str):
    s = ArrayStack(100)
    line_number = 1
    char_number = 0

    for char in input_str:
        char_number += 1
        if char == '\n':
            line_number += 1
            char_number = 0
        if char in "({[":
            s.push((char, line_number, char_number))
        elif char in ")}]":
            if s.isEmpty():
                return (1, line_number, char_number)
            top, top_line, top_char = s.pop()
            if not is_pair(top, char):
                return (2, line_number, char_number)

    if not s.isEmpty():
        top, top_line, top_char = s.pop()
        return (3, top_line, top_char)

    return 0

def is_pair(opening, closing):
    return (opening == '(' and closing == ')') or \
           (opening == '{' and closing == '}') or \
           (opening == '[' and closing == ']')

msg = input("입력 문자열: ")
result = checkBrackets(msg)
if result == 0:
    print("괄호가 맞게 닫혔습니다.")
else:
    error_code, error_line, error_char = result
    if error_code == 1:
        print(f"조건 오류 {error_code}: 닫는 괄호가 일치하지 않습니다. 라인 {error_line}, 문자 {error_char}.")
    elif error_code == 2:
        print(f"조건 오류 {error_code}: 괄호가 일치하지 않습니다. 라인 {error_line}, 문자 {error_char}.")
    elif error_code == 3:
        print(f"조곤 오류 {error_code}: 열리는 괄호가 닫히지 않았습니다. 라인 {error_line}, 문자 {error_char}.")


