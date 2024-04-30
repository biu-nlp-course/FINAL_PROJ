import matplotlib.pyplot as plt
import json
import re

with open('./results_from_models/gemma_7b_results_closed_questiones.json') as f:
    closed_questions = json.load(f)

def evaluate(Y, Y_H, arrangement_prompts=False):
    predictions = [evaluate_prompt(y, y_hat) for y, y_hat in zip(Y, Y_H)]
    accuracy = sum(predictions) / len(predictions)
    return accuracy


def evaluate_prompt(y, y_hat, arrangement_prompt=False):
    if arrangement_prompt:
        for arrangement in y_hat:
            if arrangement not in y:
                return False
        return True

    # Either num of arrangements n==m OR answer == gold answer
    return y_hat.lower() == y.lower()


def plot_results(results, title='Performance on Different Setups'):
    setups = [item[0] for item in results]
    accuracies = [item[1] for item in results]

    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    bars = plt.bar(setups, accuracies, color='skyblue', alpha=0.7, width=0.4)  # Adjust width for thinner bars
    plt.xlabel('Setups')
    plt.ylabel('Accuracy')
    plt.title(title)

    # Rotating x-axis labels diagonally
    plt.xticks(rotation=45, ha='right')

    # Adding text labels near the bars
    for i, bar in enumerate(bars):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f"{accuracies[i]:.2f}", ha='center', va='bottom',
                 fontweight='bold')

    # Display the plot
    plt.tight_layout()
    plt.grid()
    plt.savefig('fig.png')
    plt.show()


def extract_closed_questions_answers(q_results):
    """
    Extracts answers from a list of questions results.

    Args:
    - q_results (list): List of question results.

    Returns:
    - answers (list): List of extracted answers.
    """
    answers = []
    for i, question in enumerate(q_results):
        # Define regular expression patterns
        d = [181]
        pattern_answer_bold = r"\*\*Answer:\*\*(?:[ \n])(.+?)\n"
        pattern_answer_square_brackets = r"\[Answer: (.+?)\]"
        pattern_answer_text = r"The answer is:? (\w+)."

        # Try different patterns to extract the answer
        match_answer_bold = re.search(pattern_answer_bold, question)
        match_answer_square_brackets = re.search(pattern_answer_square_brackets, question)
        match_answer_text = re.search(pattern_answer_text, question)

        # Extract the answer if a match is found
        if match_answer_bold:
            extracted_text = match_answer_bold.group(1).lower()
        elif match_answer_square_brackets:
            extracted_text = match_answer_square_brackets.group(1).lower()
        elif match_answer_text:
            extracted_text = match_answer_text.group(1).lower()
        else:
            raise ValueError("No answer found for question:", question)

        answers.append(extracted_text)

    return answers


if __name__ == '__main__':
    closed_questions = closed_questions["model_full_answers"]
    answers = extract_closed_questions_answers(closed_questions)
    for i, answer in enumerate(answers, 1):
        if answer not in ['yes', 'no', 'neutral', 'true', 'false', 'entail', 'not entail']:
            print("ERROR")
            raise ValueError(f"No answer found for question {i}")
    print(answers)