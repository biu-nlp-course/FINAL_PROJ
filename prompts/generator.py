import json

spatial_conclusion_template = "{} is to the left of {}"

class MultiChoiceSpatialPromptGenerator:
    def __init__(self):
        self.data_file_path = 'OUTPUTTED_DATASETS/spatial_multi_50_passages.json'
        with open(self.data_file_path, 'r') as json_file:
            self.json_data = json.load(json_file)
        self.prompts = [
            "You are given a pair of texts. Say about this pair: given Text 1, is Text 2 true, false or neutral "
            "(you can’t tell if it’s true or false)? Reply in one word. Text 1: {} Text 2: {}"]

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
                    query = prompt.format(text_1, text_2)
                    expected_answer = conclusion[1].lower()
                    results.append((query, expected_answer))
        return results
