# Step 9
# In pascal case, strings begin with a capital letter. After converting all the characters to lowercase and adding an underscore to them, there's a chance of having an extra underscore at the start of your string.

# The easiest way to fix this is by using the .strip() string method, which removes from a string any leading or trailing characters among a set of characters passed as its argument. For example:

# Example Code
# original_string = "_example_string_"

# clean_string = original_string.strip('_')
# The strip() method is applied to original_string. This removes any leading and trailing underscore. The result of the example above would be the string 'example_string'.

# Declare a new variable named clean_snake_cased_string and assign it the result of the .strip() method applied to snake_cased_string , passing '_' as the argument to the method.


