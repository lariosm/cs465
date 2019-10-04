def encode(input_string):
    index = 0
    letter_count = 1
    compressed_string = ""

    while index < len(input_string) - 1:
        if(index == 0):
            compressed_string = input_string[0]

        #Is the letter in the next index the same as the letter in the current index?
        if(input_string[index] == input_string[index + 1]):
            letter_count += 1 #increments letter_count

        else:
            if(letter_count > 1):
                compressed_string += str(letter_count)
                letter_count = 1
            compressed_string += input_string[index + 1]

        index += 1

        if(index == len(input_string) - 1 and letter_count > 1):
            compressed_string += str(letter_count)

    if(len(compressed_string) > 0):
        return compressed_string
    
    return input_string