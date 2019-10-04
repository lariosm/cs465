def encode(input_string):
    index = 0
    letter_count = 1

    while index < len(input_string) - 1:
        if(input_string[index] == input_string[index + 1]):
            letter_count += 1 #increments letter_count
            index += 1 #moves index to next element
            continue
        index += 1
    
    if(letter_count > 1):
        return input_string[index] + str(letter_count)
    
    return input_string