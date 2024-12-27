# Step 10
# To wrap up the function, return the clean_snake_cased_string. This will complete the function and allow you to use it to convert strings from pascal or camel case to snake case.

# Add a return statement at the end of the function to return the clean_snake_cased_string.

def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
            converted_character = '_' + char.lower()
            snake_cased_char_list.append(converted_character)
        else:
            snake_cased_char_list.append(char)
    snake_cased_string = ''.join(snake_cased_char_list)
    clean_snake_cased_string = snake_cased_string.strip('_')
    return clean_snake_cased_string                     # step 10
