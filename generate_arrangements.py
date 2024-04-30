from arrangements.multi_choice_generator import MultiChoiceGenerator
from arrangements.single_choice_generator import SingleChoiceGenerator
import json


def generate_data(k=50, multi=False, disambiguate=False, temporal_reasoning=True, nodes_num=4):
    if multi:
        generator = MultiChoiceGenerator(disambiguate=disambiguate, temporal_reasoning=temporal_reasoning)
    else:
        generator = SingleChoiceGenerator(disambiguate=disambiguate, temporal_reasoning=temporal_reasoning)

    output_file = f"OUTPUTTED_SCENARIOS/"
    output_file += "temporal_" if temporal_reasoning else "spatial_"
    output_file += "multi" if multi else "single"
    output_file += "_disambiguate" if disambiguate else ""
    output_file += f"_{k}_passages"
    output_file += ".json"

    output = []
    for i in range(k):
        graph = generator.create_directed_path_graph(nodes_num)
        passage = generator.generate_passage(graph, draw_graph=False)
        output.append(passage)

    with open(output_file, "w") as json_file:
        json.dump(output, json_file)


if __name__ == '__main__':
    number_of_scenarios = 1
    for multi in [False, True]:
        for temporal_reasoning in [False, True]:
            for disambiguate in [False, True]:
                generate_data(number_of_scenarios, multi=multi, disambiguate=disambiguate,
                              temporal_reasoning=temporal_reasoning)
