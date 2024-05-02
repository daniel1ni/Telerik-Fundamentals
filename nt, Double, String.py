user_input_type = input()
user_input = input()
converted_input = None

if user_input_type == "integer":
    converted_input = int(user_input)
    converted_input += 1
elif user_input_type == "real":
     converted_input = float(user_input)
     converted_input = round((converted_input),2) + 1
     converted_input = format(converted_input,".2f")
else:
    converted_input = str(user_input)
    converted_input += "*"

print(converted_input)