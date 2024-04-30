import json

query_data_files = ["OUTPUTTED_PROMPTS/queries_closed_questiones.json", "OUTPUTTED_PROMPTS/queries_open_questions.json"]
evaluation_files = ['results_from_models/evaluation_data/closed_evaluation_data.json', 'open_evaluation_data.json']

closed_questions_data_file = query_data_files[0]
closed_questions_evaluation_file = evaluation_files[0]
with open(closed_questions_data_file, 'r') as json_file:
    queries_data = json.load(json_file)

with open(closed_questions_evaluation_file, 'r') as json_file:
    results_data = json.load(json_file)

source_file_names = queries_data['arrangement_file_source']
with_disambiguating_terms = [('disambiguate' in name) for name in source_file_names]
single_arrangement_scenario = [('single' in name) for name in source_file_names]
multi_arrangement_scenario = [('multi' in name) for name in source_file_names]
temporal_arrangement = [('temporal' in name) for name in source_file_names]
spatial_arrangement = [('spatial' in name) for name in source_file_names]

setup = results_data['setup']
question_type_binary_relation = [('binary' in name) for name in setup]
question_type_candidate = [('candidate' in name) for name in setup]

prompt_sub_type = []
prompts_sub_types_extended = queries_data['prompt_sub_type']
for subtype in prompts_sub_types_extended:
    if 'text1_text2_neutral' in subtype:
        prompt_sub_type.append("true_false_neutral")
    elif 'entail_not_entail' in subtype:
        prompt_sub_type.append('entail_not_entail')
    elif 'context_question' in subtype:
        prompt_sub_type.append("yes_no_dont_know")
    elif 'text1_text2_unable_to_determine' in subtype:
        prompt_sub_type.append("true_false_unable_to_determine")
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

i=1

with open('results_from_models/evaluation_data/closed_evaluation_data_enriched.json', "w") as json_file:
    json.dump(results_data, json_file)


