import json

with open('prompts/prompts.json', 'r') as prompts_json_file:
    prompts_json = json.load(prompts_json_file)

spatial_conclusion_template = "{} is to the left of {}"

class MultiChoiceSpatialPromptGenerator:
    def __init__(self):
        self.data_file_path = 'OUTPUTTED_DATASETS/spatial_multi_50_passages.json'
        with open(self.data_file_path, 'r') as json_file:
            self.json_data = json.load(json_file)
        yes_no_prompts = prompts_json["YES-NO PROMPTS"]
        self.prompts = [yes_no_prompts["text1_text2_neutral"], yes_no_prompts["entail_not_entail"],
                        yes_no_prompts["context_question"], yes_no_prompts["text1_text2_unable_to_determine"]]

    def get_prompts_and_expected_answers(self):
        results = []
        for item in self.json_data:
            premises = item['premises']
            text_1 = " ".join(premises)
            possible_conclusions = item['possible_conclusions']
            for conclusion in possible_conclusions:
                names = conclusion[0]
                text_2 = spatial_conclusion_template.format(names[0], names[1])
                for prompt in self.prompts:
                    query = prompt["prompt"].format(text_1, text_2)
                    expected_answer = prompt["mapping"][conclusion[1]]
                    results.append((query, expected_answer))
        return results
