first_number = int(input('Whats your 1st number?')) # add validation of number later
operation =  input('What is the operation?')
second_number = int(input('Whats your 2nd number?'))# add validation of number later

def validate_operation(operation):
    if operation == ('x'):
        return True
    elif operation == ('+'):
        return True
    elif operation == ('-'):
        return True
    elif operation == ('/'):
        return True
    else:
        return False

# This function will add the 2 inputs together
def calculation_add(first_number, operation, second_number):
    return first_number + second_number

# This function will subtract the 2 inputs together
def calculation_subtract(first_number, operation, second_number):
    return first_number - second_number

# This function will multiply the 2 inputs together
def calculation_multiply(first_number, operation, second_number):
    return first_number * second_number

# This function will divide the 2 inputs together
def calculation_divide(first_number, operation, second_number):
    return first_number / second_number

# This is for stretch goal
#def calculation(first_number, operation, second_number):
#    return first_number operation second_number

if operation == '+':
    print (calculation_add (first_number, operation, second_number))
elif operation == '-':
    print (calculation_subtract (first_number, operation, second_number))
elif operation == 'x':
    print (calculation_multiply (first_number, operation, second_number))
elif operation == '/':
    print (calculation_divide (first_number, operation, second_number))
else:
    print ('This should never happen???')
