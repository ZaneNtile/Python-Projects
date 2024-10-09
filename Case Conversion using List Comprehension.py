#List Comprehension is a construct that allows you to generate a new list by applying an expression to each item in an existing iterable and optionally filtering items with a condition

#Function to code conversion of camelcase
def convert_to_snake_case(pascal_or_camel_cased_string):

    #List Comprehension adds '_' to uppercase of iteration of argument
    snake_cased_char_list = [
        #Add conditional statement to List Comprehension 
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    #Remove first and last '_' and join all elements of variable
    return ''.join(snake_cased_char_list).strip('_')

# Function that camelCase enters for conversion
def main():
    print(convert_to_snake_case('aLongAndComplexString'))

#Call converted case
main()