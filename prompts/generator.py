import json

with open('prompts/prompts.json', 'r') as prompts_json_file:
    prompts_json = json.load(prompts_json_file)

spatial_prefix_premise = "a few people are standing in a row. "
temporal_prefix_premise = "a few people arrived to a party. "
spatial_conclusion_template = "{} is to the left of {}"
temporal_conclusion_template = "{} arrived to party before {}"
temporal_order_template = "a possible order of arrival to is {}. one after the other."
spatial_order_template = "a possible arrangement of the row from left to right is {}."


class PromptGenerator:
    def __init__(self, arrangements_file_path, prompt_question_type):
        if 'spatial' in arrangements_file_path:
            self.text_2_template = spatial_conclusion_template
            self.premises_prefix = spatial_prefix_premise
            self.possible_order_template = spatial_order_template
        elif 'temporal' in arrangements_file_path:
            self.text_2_template = temporal_conclusion_template
            self.premises_prefix = temporal_prefix_premise
            self.possible_order_template = temporal_order_template
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
            text_1 = self.premises_prefix + " ".join(premises)
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
                    prompts_sub_types.append("binary_relation_" + prompt_subtype)
            possible_arrangements = arrangement['possible_arrangements']
            for possible_arrangement in possible_arrangements:
                order = ", ".join(possible_arrangement)
                text_2 = self.possible_order_template.format(order)
                for prompt_subtype, prompt_template in self.prompts_templates:
                    query = prompt_template["prompt"].format(text_1, text_2)
                    expected_answer = prompt_template["mapping"]["TRUE"]
                    prompts.append(query)
                    expected_answers.append(expected_answer)
                    arrangements_internal_nums.append(arrangements_idx)
                    prompts_sub_types.append('possible_arrangements_' + prompt_subtype)
        return prompts_sub_types, arrangements_internal_nums, prompts, expected_answers


class OpenQuestionPromptGenerator(PromptGenerator):
    def get_prompts_and_expected_answers(self):
        #todo build this
        return None
