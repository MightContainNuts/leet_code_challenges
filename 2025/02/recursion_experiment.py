


def recursion_factorial(num:int)->int:
    """ returns the factorial of a number using recursion"""
    if num == 1 or num ==0:
        return 1
    return recursion_factorial(num-1)*num


def recursion_fibonaci(num:int)->int:
    """returns the fibonaci number using recusrsion"""
    if num == 0:
        return 0
    if num == 1:
        return 1
    return recursion_fibonaci(num-1) + recursion_fibonaci(num-2)


def sum_of_digits(num:int)->int:
    """returns sum of digits"""
    if num == 0:
        return 0
    return num + sum_of_digits(num-1)


if __name__ == '__main__':
    print(recursion_factorial(10))
    print(recursion_fibonaci(10))
    print(sum_of_digits(10))
