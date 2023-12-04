import sys, os
from pathlib import Path

current_file = Path(__file__).resolve()  # Get the absolute path of the current script
project_root = current_file.parents[1]   # Go two levels up to get to 'year2023'

sys.path.append(str(project_root))       # Add the 'year2023' directory to the system path
from input_analyzer import convert_as_plain_array as get_data  # Import from 'year2023'


'''
The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

'''

inputfile = 'input.txt'
current_script_path = os.path.abspath(__file__)
absolute_file_path = os.path.join(os.path.dirname(current_script_path), inputfile)


def findNumberPairsPerEntryAndSum():
    ans = []
    for entry in get_data(absolute_file_path):
        l_digit = ""
        r_digit = ""
        for c in entry:
            if c.isdigit():
                l_digit = c
                break
        for c in reversed(entry):
            if c.isdigit():
                r_digit = c
                break
        ans.append(int(l_digit + r_digit))

    # tally numbers
    final = sum(ans)
    return final

def solution():
    ans = []
    words = {
        "one" : "1",
        "two" : "2",
        "three" : "3",
        "four" : "4",
        "five" : "5",
        "six" : "6",
        "seven" : "7",
        "eight" : "8",
        "nine" : "9",
    }
    # this approach uses fixed iterator instead of sliding window, cause substr will always be len 5 or less
    for entry in get_data(absolute_file_path):
        l_digit = ""
        r_digit = ""
        for i in range(len(entry) - 4):
            current = entry[i: i+5]
            for c in current:
            # not the most efficient having a inner loop checking for a num but oh well
                if c.isdigit():
                    l_digit = c
                    break
            if current in words:
                l_digit = words[current]
                break
        # could also use a string reverse, but would allocate additional O(n) time, space
        for i in range(len(entry) - 4, -1, -1):
            if i - 4 >= 0: #guaranteed we have a num, but might as well handle ensuring we have enough chars
                current = entry[i-4: i+1]
                for c in current:
                    if c.isdigit():
                        r_digit = c
                        break
                if current in words:
                    r_digit = words[current]
                    break


        ans.append((l_digit + r_digit))

    # tally numbers
    final = sum(ans)
    return final

# solution()
print(solution())