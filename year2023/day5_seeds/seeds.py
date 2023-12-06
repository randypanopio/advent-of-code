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
    seeds = []
    mappings_table = {}

    for index, prop in enumerate(properties):
        sbs = prop.split(":")
        key = sbs[0]
        # 0 is seeds
        if index == 0:
            seeds = [int(e) for e in sbs[1].split()]
        else:
            ans = []
            for range in sbs[1].split("\n"):
                if range: #discard empty
                    sub = []
                    for num in range.split(" "):
                        sub.append(int(num))
                    ans.append(sub)

            mappings_table[key] = ans

    shortest = 2**32

    for seed in seeds:
        current = seed
        print(f"seed: {seed}")
        for mapping_name, mapping in mappings_table.items():
            for lookup in mapping:
                s_start = lookup[0]
                range_length = lookup[2]
                ds_start = lookup[1]
                if current >= ds_start and (current < range_length + ds_start):
                    print(f"in bounds of the closest mapping {mapping_name} (starting range at) {s_start}  moving from {current} to {current - ds_start + s_start}")
                    current = current - ds_start + s_start # move to new mapping continue to next lookup
                    break
        print(f"final mapped position: {current}")
        shortest = min(current, shortest)
    return shortest

result = parse_property_values()
print(result)


