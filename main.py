from multi_choice_generator import MultiChoiceGenerator
from single_choice_generator import SingleChoiceGenerator
import json


def generate_data(k=50, multi=False, disambiguate=False):
    if multi:
        generator = MultiChoiceGenerator(disambiguate=disambiguate)
    else:
        generator = SingleChoiceGenerator(disambiguate=disambiguate)

    output_file = f"OUTPUTTED_DATASETS/"
    output_file += "multi" if multi else "single"
    output_file += "_disambiguate" if disambiguate else ""
    output_file += f"_{k}passages"
    output_file += ".json"

    output = []
    for i in range(k):
        n = 4
        graph = generator.create_directed_path_graph(n)
        passage = generator.generate_passage(graph, draw_graph=False)
        output.append(passage)

    with open(output_file, "w") as json_file:
        json.dump(output, json_file)


if __name__ == '__main__':
    generate_data(50, multi=False, disambiguate=False)
    generate_data(50, multi=False, disambiguate=True)
    generate_data(50, multi=True, disambiguate=False)
    generate_data(50, multi=True, disambiguate=True)
