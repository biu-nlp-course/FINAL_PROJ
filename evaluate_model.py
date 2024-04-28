import os
from together import Together
import json
from prompts.generator import MultiChoiceSpatialPromptGenerator

client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))
write_queries_to_file = True


queries = MultiChoiceSpatialPromptGenerator().get_prompts_and_expected_answers()

if write_queries_to_file:
    with open("./queries.txt", "w") as f:
        for prompt, expected_answer in queries:
            f.write(f"{'*' * 100}\n{prompt}{'-' * 30}\nExpected answer: {expected_answer}\n{'*' * 100}\n\n")

for query, answer in queries:
    response = client.chat.completions.create(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        messages=[{"role": "user", "content": query}],
    )

    print(response.choices[0].message.content)