# Step 8
# By this point, the variable snake_cased_char_list holds the list of converted characters. To combine these characters into a single string, you can utilize the .join() method.

# The join method works by concatenating each element of a list into a string, separated by a designated string, known as the separator.

# Example Code
# result_string = ''.join(characters)
# The example above joins together the elements of the characters list into a single string where each element is concatenated together using an empty string as the separator.

# Now, right after the for loop, use the .join() method to join the elements in snake_cased_char_list using an empty string as the separator. Assign the result to a new variable named snake_cased_string.

def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
            converted_character = '_' + char.lower()
            snake_cased_char_list.append(converted_character)
        else:
            snake_cased_char_list.append(char)
    snake_cased_string = "".join(snake_cased_char_list)             # step 8
