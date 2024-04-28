import os
from together import Together

from prompts.generator import MultiChoiceSpatialPromptGenerator

client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

queries = MultiChoiceSpatialPromptGenerator().get_prompts_and_expected_answers()

for query, answer in queries:
    response = client.chat.completions.create(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        messages=[{"role": "user", "content": query}],
    )

    print(response.choices[0].message.content)