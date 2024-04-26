from multi_choice_generator import MultiChoiceGenerator
from single_choice_generator import SingleChoiceGenerator
import json

def generate_data(k=50, multi=False, disambiguate=False, temporal_reasoning=True):
    if multi:
        generator = MultiChoiceGenerator(disambiguate=disambiguate, temporal_reasoning=temporal_reasoning)
    else:
        generator = SingleChoiceGenerator(disambiguate=disambiguate, temporal_reasoning=temporal_reasoning)

    output_file = f"OUTPUTTED_DATASETS/"
    output_file += "temporal_" if temporal_reasoning else "spatial_"
    output_file += "multi" if multi else "single"
    output_file += "_disambiguate" if disambiguate else ""
    output_file += f"_{k}_passages"
    output_file += ".json"

    output = []
    for i in range(k):
        N = 4
        graph = generator.create_directed_path_graph(N)
        passage = generator.generate_passage(graph, draw_graph=False)
        output.append(passage)

    with open(output_file, "w") as json_file:
        json.dump(output, json_file)


if __name__ == '__main__':
    generate_data(50, multi=False, disambiguate=False, temporal_reasoning=True)
    generate_data(50, multi=False, disambiguate=True, temporal_reasoning=True)
    generate_data(50, multi=True, disambiguate=False, temporal_reasoning=True)
    generate_data(50, multi=True, disambiguate=True, temporal_reasoning=False)