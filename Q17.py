# Step 17
# Instead of returning the list snake_cased_char_list, you will need to join its elements into a single string using an empty string '' as the separator.

# Modify the return statement to return the result of joining snake_cased_char_list with an empty string as a separator.


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
    

    return ''.join(snake_cased_char_list)               # step 17


def main():
    print(convert_to_snake_case('aLongAndComplexString'))

main()