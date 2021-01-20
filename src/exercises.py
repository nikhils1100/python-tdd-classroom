def reverse_list(input_list):
    """
    Reverses order of elements in list input_list.
    """
    input_list_len = len(input_list)

    for i in range(input_list_len//2):
        tmp = input_list[i]
        input_list[i] = input_list[input_list_len-i-1]
        input_list[input_list_len-i-1] = tmp

    return input_list

def count_digits(number):
    """
    Return count of digits
    """
    if number>=0 and number<1:
        return 0
    
    no_digits = 0
    if number < 0:
        number = -number

    while number >= 1:
        no_digits += 1
        number /= 10

    return no_digits