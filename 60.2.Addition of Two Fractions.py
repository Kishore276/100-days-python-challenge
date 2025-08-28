from fractions import Fraction

def add_fractions(num1, denom1, num2, denom2):
    # Using the Fraction class to handle addition and simplification
    fraction1 = Fraction(num1, denom1)
    fraction2 = Fraction(num2, denom2)
    result = fraction1 + fraction2
    return result.numerator, result.denominator
num1, denom1 = 1, 2 
num2, denom2 = 1, 3 
result_numerator, result_denominator = add_fractions(num1, denom1, num2, denom2)
print(f"The sum of {num1}/{denom1} and {num2}/{denom2} is: {result_numerator}/{result_denominator}")