def closure(number):

    def nested_function(text):
        return text * number

    return nested_function


variable = closure(6) # variable = nested_function
print(variable("jestem w srodku - "))