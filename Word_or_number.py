user_input = input()
reversed_string = ""

def is_Float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def is_Integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


if is_Integer(user_input) == True:
    print(int(user_input)+1)
elif is_Float(user_input) == True:
    result = float(user_input) + 1
    formatted_result = format(result,".2f")
    print(formatted_result)
else:
    reversed_string = user_input[::-1]
    print(reversed_string)
