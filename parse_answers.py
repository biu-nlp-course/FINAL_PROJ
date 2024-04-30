import json
import os


def sort_possible_arrangements():
    arrangements_files = ['OUTPUTTED_ARRANGEMENTS/' + file_name for file_name in os.listdir("OUTPUTTED_ARRANGEMENTS")]
    for arrangements_file in arrangements_files:
        new_arrangements = []
        with open(arrangements_file, 'r') as json_file:
            arrangements_data = json.load(json_file)
        for arrangement in arrangements_data:
            sorted_arrangements = sorted(arrangement['possible_arrangements'])
            arrangement['possible_arrangements'] = sorted_arrangements
            new_arrangements.append(arrangement)

        with open(arrangements_file, "w") as json_file:
            json.dump(new_arrangements, json_file)
