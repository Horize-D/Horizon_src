def replace_dot_with_heart(input_string):
    replaced_string = input_string.replace('。', '♥')
    return replaced_string

input_message = input("文章を入力\n")

result = replace_dot_with_heart(input_message)
print(result)
