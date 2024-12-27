# Step 18
# After joining the elements of the list snake_cased_char_list, you will need to remove any leading or trailing underscores from the resulting string. For this, use the strip method with the underscore character _ as an argument.

# Method calls can be chained together, which means that the result of one method call can be used as the object for another method call.

# Example Code
# words_list = ['hello', 'world', 'this', 'is', 'chained', 'methods']
# result = ' '.join(words_list).upper()
# In the example above, the .upper() method is chained to ' '.join(words_list), therefore .upper() is called on the result of the .join() call.

# Modify the return statement by chaining to ''.join(snake_cased_char_list) a call to the .strip() method to remove any leading or trailing underscores.


def convert_to_snake_case(pascal_or_camel_cased_string):
    # snake_cased_char_list = []
    # for char in pascal_or_camel_cased_string:
    #     if char.isupper():
    #       converted_character = '_' + char.lower()
    #       snake_cased_char_list.append(converted_character)
    #     else:
    #         snake_cased_char_list.append(char)
    # snake_cased_string = ''.join(snake_cased_char_list)
    # clean_snake_cased_string = snake_cased_string.strip('_')

    # return clean_snake_cased_string

    snake_cased_char_list = []
    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('aLongAndComplexString'))

main()