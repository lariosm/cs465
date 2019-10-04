def encode(input_string):
    index = 0
    letter_count = 1
    compressed_string = ""

    while index < len(input_string) - 1:
        #Is the letter in the next index the same as the letter in the current index?
        if(input_string[index] == input_string[index + 1]):
            letter_count += 1 #increments letter_count
            #index += 1 #moves index to next element

        if(input_string[index] != input_string[index + 1]):
            if(letter_count > 1):
                compressed_string += input_string[index] + str(letter_count)
                letter_count = 1 #Resets letter_count to 1 for next set of repeating letters
        
        index += 1

    if(letter_count > 1):
        compressed_string += input_string[index] + str(letter_count)

    if(len(compressed_string) > 0):
        return compressed_string
    
    return input_string