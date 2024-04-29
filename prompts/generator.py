import json

with open('prompts/prompts.json', 'r') as prompts_json_file:
    prompts_json = json.load(prompts_json_file)

spatial_conclusion_template = "{} is to the left of {}"
temporal_conclusion_template = "{} arrived to party before {}"


class PromptGenerator:
    def __init__(self, arrangements_file_path, prompt_question_type):
        if 'spatial' in arrangements_file_path:
            self.text_2_template = spatial_conclusion_template
        elif 'temporal' in arrangements_file_path:
            self.text_2_template = temporal_conclusion_template
        with open(arrangements_file_path, 'r') as json_file:
            self.arrangements_data = json.load(json_file)
        self.prompts_templates = list(prompts_json[prompt_question_type].items())


class EntailmentPromptGenerator(PromptGenerator):
    def get_prompts_and_expected_answers(self):
        prompts = []
        expected_answers = []
        arrangements_internal_nums = []
        prompts_sub_types = []
        for arrangements_idx, arrangement in enumerate(self.arrangements_data):
            premises = arrangement['premises']
            text_1 = " ".join(premises)
            possible_conclusions = arrangement['possible_conclusions']
            for conclusion in possible_conclusions:
                names = conclusion[0]
                text_2 = self.text_2_template.format(names[0], names[1])
                for prompt_subtype, prompt_template in self.prompts_templates:
                    query = prompt_template["prompt"].format(text_1, text_2)
                    expected_answer = prompt_template["mapping"][conclusion[1]]
                    prompts.append(query)
                    expected_answers.append(expected_answer)
                    arrangements_internal_nums.append(arrangements_idx)
                    prompts_sub_types.append(prompt_subtype)
        return arrangements_internal_nums, prompts, expected_answers


class OpenQuestionPromptGenerator(PromptGenerator):
    def get_prompts_and_expected_answers(self):
        return None
