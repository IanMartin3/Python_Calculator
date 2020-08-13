first_number = input('Whats your 1st number?')
second_number = input('Whats your 2nd number?')
operation =  input('What is the operation?')

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

print ('testing validate_operation')
print (validate_operation (operation) )