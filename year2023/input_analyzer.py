'''
utils for converting inputs for my solutions
'''

def convert_as_plain_array(file_path):
    '''
    returns each line as an entry to the array
    '''
    with open(file_path) as file:
        return [line.rstrip() for line in file]