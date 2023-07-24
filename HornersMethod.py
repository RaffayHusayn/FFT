# this is O(n) way of polynomial eval 
# the idea is to simplify 2x^3 + 4x^2 + x + 4 into ((2x+4)x+1)+x+4 
# this just means iteratively multiplying the largest coefficient with value and adding the next coefficient

# when value = 2 ->    16 + 16 + 6 = 37


def hornersMethod(coefficients, value):
    length = len(coefficients)
    result = coefficients[length-1] 
    for i in reversed(range(1, length)):
        result = (result * value) + coefficients[i-1]

    return result

print(hornersMethod([-1, 2 , -6, 2], 3))

