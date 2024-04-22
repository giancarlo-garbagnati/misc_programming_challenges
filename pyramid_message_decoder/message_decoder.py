import math

def decode_file(message_file):
    """ `message_file` should be a file object read in by a call to open(..., 'r').
    I wasn't clear if the prompt wanted a file object or a string as a parameter. If 
    the string parameter is needed, you can use the function below (`decode_string`),
    which this function calls.
    
    Assumes the `message_file` contains no duplicate numbers and is sequential from 1
    to n (with n being the highest number of the list). This should be able to parse 
    "incomplete" pyramids, such as:
         1
        2 3
       4 5
    Where the final output (per the instructions "The key to decoding the message is to 
    use the words corresponding to the numbers at the end of each pyramid line") would
    be the words corresponding to these indices: 1 3 5
    """

    # Calls the function below to decode the string
    return decode_string(message_file.read())

def decode_string(message):
    """ The words that are used for the decoded message uses the triangular number 
    series: (n+1)*n/2 (assuming a full "pyramid"). This solution should account for
    both full and incomplete pyramids.
    """

    message = message.strip()

    # Converts the message string into a dictionary where the number (converted to
    # int) is stored as the key with the word stored as the value
    message_dict = {
        int(k):v for k,v in dict([
            e.split(' ') for e in message.split('\n')
        ]).items()
    }

    # Highest number (should also be the length of the dict, since the numbers should
    # be sequential)
    max_no = max(message_dict.keys())

    # This variable determines the length of the final message (ie how many rows
    # there are in the pyramid) by taking the triangular number series equation
    # and setting it equal to the `max_no` (largest number in the message), then 
    # solving for n. If the pyramid is full, that should be enough. However, for
    # incomplete pyramids, we'll have to take that fraction and get the ceiling 
    # of it.
    message_len = math.ceil((-1 + math.sqrt(1+8*max_no))/2)

    # Generate the message by using the triangular number series for all rows
    # between 1 and message_len-1 (then adding the max_no as the last index).
    decoded_list = []
    for n in range(1,message_len): # to exclude 0
        decoded_list.append(message_dict[int((n+1)*(n)/2)])
    decoded_list.append(message_dict[max_no])

    return ' '.join(decoded_list)

if __name__ == "__main__":

    encoded_message_file = 'coding_qual_input.txt'
    # encoded_message_file = 'coding_qual_easy.txt'
    f = open(encoded_message_file, 'r')

    print(decode_file(f))
    