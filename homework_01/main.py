import math

def power_numbers(*args):
    return list(map(lambda x: x*x, args))


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(digit):
    sqr = math.sqrt(digit)
    sqr = math.ceil(sqr)

    if digit < 2:
        return False
    elif digit == 2:
        return True
    elif digit % 2 == 0:
        return False

    for i in range(3, sqr + 1, 2):
        if digit % i == 0:
            return False

    return True


def filter_numbers(digits, filter_type):

    if filter_type == ODD:
        return list(filter(lambda x: x % 2 != 0, digits))
    elif filter_type == EVEN:
        return list(filter(lambda x: x % 2 == 0, digits))
    else:
        return list(filter(is_prime, digits))


if __name__ == "__main__":
    print("SQR: ", power_numbers(1, 2, 3, 4, 5, 6, 7, 8))
    print("ODD: ", filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], ODD))
    print("EVEN: ", filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], EVEN))
    print("PRIME: ", filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 19, 20, 21, 23, 25, 27, 29], PRIME))
