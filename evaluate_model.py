import json
import os
from together import Together

from prompts.generator import EntailmentPromptGenerator

client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))
write_queries_to_file = True

arrangements_files = ['OUTPUTTED_DATASETS/' + file_name for file_name in os.listdir("OUTPUTTED_DATASETS")]

with open('prompts/prompts.json', 'r') as prompts_file:
    prompts_dict = json.load(prompts_file)
prompt_question_types = list(prompts_dict.keys())

queries_data = {
    'arrangement_file_source': [],
    'prompt_type': [],
    'arrangement_idx_in_file': [],
    'prompt': [],
    'expected_answer': []
}

for arrangements_file in arrangements_files:
    for prompt_question_type in prompt_question_types:
        if 'temporal' in prompt_question_type:
            if 'spatial' in arrangements_file:
                pass
        elif 'spatial' in prompt_question_type:
            if 'temporal' in arrangements_file:
                pass

        if prompt_question_type in ["YES-NO PROMPTS"]:
            arrangements_ids, prompts, expected_answers = (
                EntailmentPromptGenerator(arrangements_file, prompt_question_type).
                get_prompts_and_expected_answers())
        else:
            # arrangements_ids, prompts, expected_answers = ()
            break
        length = len(prompts)
        arrangement_file_sources = [arrangements_file] * length
        prompt_types = [prompt_question_type] * length
        queries_data['arrangement_file_source'].extend(arrangement_file_sources)
        queries_data['prompt_type'].extend(prompt_types)  # todo get full type of prompt, with subtype
        queries_data['arrangement_idx_in_file'].extend(arrangements_ids)
        queries_data['prompt'].extend(prompts)
        queries_data['expected_answer'].extend(expected_answers)

if write_queries_to_file:
    with open("./queries.json", 'w') as json_file:
        json.dump(queries_data, json_file)

prompts = queries_data['prompt']
expected_answers = queries_data['expected_answer']
experiment_data = zip(prompts, expected_answers)

if write_queries_to_file:
    with open("./queries.txt", "w") as f:
        for prompt, expected_answer in experiment_data:
            f.write(f"{'*' * 100}\n{prompt}{'-' * 30}\nExpected answer: {expected_answer}\n{'*' * 100}\n\n")

model_answers = []
for prompt, expected_answer in experiment_data:
    response = client.chat.completions.create(
        model="google/gemma-2b-it",
        messages=[{"role": "user", "content": prompt}],
    )
    answer = response.choices[0].message.content
    print(answer)
    model_answers.append(answer)
