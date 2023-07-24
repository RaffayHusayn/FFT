# Brute Force way to evaluate the value of a polynomial for a value

def eval(polynomial, value):
    length = len(polynomial) 
    result = 0
    for i in range(0, length):
        result +=  polynomial[i] * pow(value, i) 

    return result




print(eval([2,3,4], 2))

