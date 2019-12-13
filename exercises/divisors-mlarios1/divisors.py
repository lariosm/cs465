def divisors(num):
    divisor_list = []
    for index in range(num):
        if num % (index + 1) == 0:
            divisor_list.append(index + 1)
    return divisor_list
