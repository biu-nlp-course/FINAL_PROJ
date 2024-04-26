import json


# read json into memory
# for each line,
    # generate type 1 first section of prompt, then for each possible conclusion insert it
    # perform query
    # parse answer

json_file_path = 'OUTPUTTED_DATASETS/spatial_multi_50_passages.json'
with open(json_file_path, 'r') as json_file:
    json_data = json.load(json_file)

i = 1

prompts = ["You are given a pair of texts. Say about this pair: given Text 1, is Text 2 true, false or neutral "
           "(you can’t tell if it’s true or false)? Reply in one word. Text 1: {} Text 2: {}"]

# formatted_string = "Hello, my name is {} and I am {} years old.".format(name, age)

spatial_conclusion_template = "{} is to the left of {}"
results = []

for item in json_data:
    premises = item['sentences']
    text_1 = " ".join(premises)
    possible_conclusions = item['possible_conclusions']
    for conclusion in possible_conclusions:
        names = conclusion[0]
        text_2 = spatial_conclusion_template.format(names[0], names[1])
        for prompt in prompts:
            query = prompt.format(text_1, text_2)
            i = 1
            result = "False"







