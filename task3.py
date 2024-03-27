def check_brackets(input_string):
    stack = []
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    brackets_map = {')': '(', ']': '[', '}': '{'}
    
    for char in input_string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if len(stack) == 0:
                return False
            if stack[-1] == brackets_map[char]:
                stack.pop()
            else:
                return False
    
    if len(stack) != 0:
        return False
    
    return True

# Пример использования:
input_string = '({[]})'
print(check_brackets(input_string))  # Результат: True

input_string = '({[)}'
print(check_brackets(input_string))  # Результат: False