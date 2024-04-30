import json
import os
import re


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


number_pattern_1 = r"The answer is (\d+)"


def parse_answers_if_possible():
    queries_data_file = 'OUTPUTTED_PROMPTS/queries_open_questions.json'
    with open(queries_data_file, 'r') as json_file:
        queries_data = json.load(json_file)
    results_data_file = 'results_from_models/gemma_7b_results_open_questions.json'
    with open(results_data_file, 'r') as json_file:
        results_data = json.load(json_file)
    full_answers = results_data['model_full_answers']
    prompt_types = queries_data['prompt_type']
    parsed_answers = []
    i = -1
    for answer, prompt_type in zip(full_answers, prompt_types):
        i += 1
        if "NUMBER" in prompt_type:
            match = re.search(number_pattern_1, answer)
            if match:
                parsed = match.group(1)
                if len(parsed) < 3:
                    parsed_answers.append(parsed)
        else:
            parsed_answers.append(f"UNPARSEBLE on index {i}")
    results_data['parsed_answers'] = parsed_answers
    with open(results_data_file, "w") as json_file:
        json.dump(results_data, json_file)


def iterate_gold_answers():
    queries_data_file = 'OUTPUTTED_PROMPTS/queries_open_questions.json'
    with open(queries_data_file, 'r') as json_file:
        queries_data = json.load(json_file)
    gold_answers = queries_data['expected_answer']
    results_data_file = 'results_from_models/gemma_7b_results_open_questions.json'
    with open(results_data_file, 'r') as json_file:
        results_data = json.load(json_file)
    parsed_answers = results_data['parsed_answers']
    full_answers = results_data['model_full_answers']
    for gold_answer, parsed_result, full_answer in zip(gold_answers, parsed_answers, full_answers):
        if "UNPARSEBLE" in parsed_result:
            print("****************************")
            print(parsed_result)
            print(f"gold:{gold_answer}")
            print("received \n")
            print(full_answer)
            i = 1


iterate_gold_answers()