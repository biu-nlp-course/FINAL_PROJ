import json
import re

evaluation_files = ['results_from_models/evaluation_data/llama_8b_evaluation_data.json']

closed_questions_data_file = evaluation_files[0]
closed_questions_evaluation_file = evaluation_files[0]

with open(closed_questions_evaluation_file, 'r') as json_file:
    results_data = json.load(json_file)


def parse_result(raw_result, idx):
    pattern_answer_square_brackets = r"^\[Answer: (.+?)\]"
    match_answer_square_brackets = re.search(pattern_answer_square_brackets, raw_result)

    if raw_result.isdigit():
        extracted_text = int(raw_result)
    elif match_answer_square_brackets:
        extracted_text = match_answer_square_brackets.group(1).lower()
    else:
        extracted_text = f'UNPARSABLE,{idx}'

    return extracted_text


source_file_names = results_data['arrangement_file_source']
with_disambiguating_terms = [('disambiguate' in name) for name in source_file_names]
single_arrangement_scenario = [('single' in name) for name in source_file_names]
multi_arrangement_scenario = [('multi' in name) for name in source_file_names]
temporal_arrangement = [('temporal' in name) for name in source_file_names]
spatial_arrangement = [('spatial' in name) for name in source_file_names]

setup = results_data['prompt_sub_type']
question_type_binary_relation = [('binary' in name) for name in setup]
question_type_candidate = [('candidate' in name) for name in setup]
question_type_show_all_possible_with_names = [(('all_possible_arrangements_with_the_names_of_the people' in name)
                                    or ('all_possible_arrangements_with_the_number_of_the_people' in name)
                                               or ('all_possible_arrangements_with_the_names_of_the_people' in name)) for name in setup]
question_type_count_all_possible_with_names = [(('num_of_all_possible_arrangements_with_the_number_of_the_people' in name)
                                    or ('num_of_all_possible_arrangements_with_the_names_of_the_people' in name) or
                                                ('num_of_all_possible_arrangements_with_the_names_of_the people' in name)) for name in setup]


prompt_sub_type = []
prompts_sub_types_extended = results_data['prompt_sub_type']
for subtype in prompts_sub_types_extended:
    if 'text1_text2_neutral' in subtype:
        prompt_sub_type.append("true_false_neutral")
    elif 'entail_not_entail' in subtype:
        prompt_sub_type.append('entail_not_entail')
    elif 'context_question' in subtype:
        prompt_sub_type.append("yes_no_dont_know")
    elif 'text1_text2_unable_to_determine' in subtype:
        prompt_sub_type.append("true_false_unable_to_determine")
    elif ('all_possible_arrangements_with_the_names_of_the' in subtype) or ('num_of_all_possible_arrangements_with_the_names_of_the_people' == subtype):
        prompt_sub_type.append("with_the_names_of_the_people")
    elif ('all_possible_arrangements_with_the_number_of_the_people' == subtype) or (
            'num_of_all_possible_arrangements_with_the_number_of_the_people' == subtype):
        prompt_sub_type.append("with_the_number_of_the_people")
    else:
        raise ValueError

results_data["with_disambiguating_terms"] = with_disambiguating_terms
results_data["single"] = single_arrangement_scenario
results_data["multi"] = multi_arrangement_scenario
results_data["temporal"] = temporal_arrangement
results_data["spatial"] = spatial_arrangement
results_data["binary_relation"] = question_type_binary_relation
results_data["candidate"] = question_type_candidate
results_data["prompt_subtype"] = prompt_sub_type
results_data["show_all_possible"] = question_type_show_all_possible_with_names
results_data["count_all_possible"] = question_type_count_all_possible_with_names
raw_results = results_data['model_full_answers']
parsed_results = [parse_result(res, i) for i, res in enumerate(raw_results)]
results_data["predictions"] = parsed_results
results_data["expected"] = results_data['expected_answer']
del results_data["expected_answer"]
results_data["success"] = [y_hat == y for y, y_hat in zip(results_data['expected'], results_data['predictions'])]


i=1

with open('results_from_models/evaluation_data/llama_8b_evaluation_data_enriched.json', "w") as json_file:
    json.dump(results_data, json_file)


