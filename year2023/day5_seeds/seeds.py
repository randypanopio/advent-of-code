import sys, os
from pathlib import Path

current_file = Path(__file__).resolve()
project_root = current_file.parents[1]
sys.path.append(str(project_root))
from input_analyzer import plain_string as get_data

inputfile = 'input.txt'
current_script_path = os.path.abspath(__file__)
absolute_file_path = os.path.join(os.path.dirname(current_script_path), inputfile)


"""

"""

def parse_property_values():
    input_string = get_data(absolute_file_path)
    properties = input_string.split('\n\n')
    result = {}

    # this is wrong lol, uh oh graph problem bruh im ded

    for index, prop in enumerate(properties):
        sbs = prop.split(":")
        key = sbs[0]
        # 0 is seeds
        if index == 0:
            result[key] = [int(e) for e in sbs[1].split()]
        else:
            ans = []
            for range in sbs[1].split("\n"):
                sub = []
                for num in range.split():
                    sub.append(int(num))
                ans.append(sub)
            result[key] = ans


    return result

result = parse_property_values()
print(result)
