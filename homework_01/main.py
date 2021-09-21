
def power_numbers(*args):
    return list(map(lambda x: x*x, args))


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(digit):
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
    print("PRIME: ", filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], PRIME))
