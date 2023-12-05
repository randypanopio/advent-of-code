import sys, os, re
from pathlib import Path

current_file = Path(__file__).resolve()  # Get the absolute path of the current script
project_root = current_file.parents[1]   # Go two levels up to get to 'year2023'

sys.path.append(str(project_root))       # Add the 'year2023' directory to the system path
from input_analyzer import convert_as_plain_array as get_data  # Import from 'year2023'


'''
You're launched high into the atmosphere! The apex of your trajectory just barely reaches the surface of a large island floating in the sky. You gently land in a fluffy pile of leaves. It's quite cold, but you don't see much snow. An Elf runs over to greet you.

The Elf explains that you've arrived at Snow Island and apologizes for the lack of snow. He'll be happy to explain the situation, but it's a bit of a walk, so you have some time. They don't get many visitors up here; would you like to play a game in the meantime?

As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.

To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.

Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?


'''
inputfile = 'input.txt'
current_script_path = os.path.abspath(__file__)
absolute_file_path = os.path.join(os.path.dirname(current_script_path), inputfile)

'''
complexity should boil down to O(n) runtime
+ O(n) traversing the "round" which are entries on input
+ O(n) traversing all the "games" of each round, and assigning the counts of each color into a dict
+ O(1) retrieving counts for each color in the generated dict
+ O(n) for summing up the indices of valid rounds
= O(3n+1) = O(n)

space complexity should boil down to O(n):
+ O(n) for the array of entries from reading file
+ O(n) for the array containing the indices of valid rounds
+ O(n) for the color count HT for each game
+ O(1) for each color retrived from the color count HT
= O(3n +1) = O(n)
'''
def count_invalid_rounds():
    color_counts = []
    for index, round  in enumerate(get_data(absolute_file_path)):
        # strip the first 'Game x: ' substring
        round[7:]
        games = round.split(';')
        # regex :shrug:
        valid_round = True
        for game in games:
            colors = re.findall(r'(\d+)\s+(\w+)', game)  # Find color counts in each game
            color_count = {color: int(count) for count, color in colors}
            red_c = 0 if not 'red' in color_count.keys() else color_count['red']
            green_c = 0 if not 'green' in color_count.keys() else color_count['green']
            blue_c = 0 if not 'blue' in color_count.keys() else color_count['blue']
            # print(f'round: {index +1}, game: {game_index}, red: {red_c}, green: {green_c}, blue: {blue_c}')
            if red_c > 12 or green_c > 13 or blue_c > 14:
                valid_round = False
                break

        print(f"round validity {valid_round} at round: {index +1}")
        if valid_round:
            # valid game, add line index
            color_counts.append(index+1)
        # my sol would be manual string parse TODO

    return color_counts


def count_fewest_cubes_of_each_round():
    cube_power = []
    for index, round  in enumerate(get_data(absolute_file_path)):
        # strip the first 'Game x: ' substring
        round[7:]
        games = round.split(';')
        # what if hteres no minimum color? then power would be zero, probs expected?
        highest_r = 0
        highest_g = 0
        highest_b = 0
        for game in games:
            colors = re.findall(r'(\d+)\s+(\w+)', game)  # Find color counts in each game
            color_count = {color: int(count) for count, color in colors}

            red_c = 0 if not 'red' in color_count.keys() else color_count['red']
            highest_r = max(highest_r, red_c)
            green_c = 0 if not 'green' in color_count.keys() else color_count['green']
            highest_g = max(highest_g, green_c)
            blue_c = 0 if not 'blue' in color_count.keys() else color_count['blue']
            highest_b = max(highest_b, blue_c)

        cube_power.append(highest_b * highest_g * highest_r)

    return cube_power

total = sum(count_fewest_cubes_of_each_round())
print(f"sum: \n{total}")
# count_invalid_rounds()

