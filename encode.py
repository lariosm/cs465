def encode(input_string):
    index = 0 #Our index counter to traverse the input string
    letter_count = 1 #A counter to keep track how often a letter is repeated
    encoded_string = "" #Where letters will be stored in their shortened form

    while index < len(input_string) - 1:
        if(index == 0):
            encoded_string = input_string[0] #Append letter from first index

        #Is the letter in the next index the same as the letter in the current index?
        if(input_string[index] == input_string[index + 1]):
            letter_count += 1 #Increment letter_count

        else:
            #Is final count for a letter greater than 1?
            if(letter_count > 1):
                encoded_string += str(letter_count) #Appends letter count
                letter_count = 1 #Reset letter counter back to 1
            encoded_string += input_string[index + 1] #Append next non-repeating letter

        index += 1 #Increment index counter

        #Have we reached the end and still need to append letter count to a repeating letter?
        if(index == len(input_string) - 1 and letter_count > 1):
            encoded_string += str(letter_count)

    if(len(encoded_string) > 0):
        return encoded_string
    
    return input_string